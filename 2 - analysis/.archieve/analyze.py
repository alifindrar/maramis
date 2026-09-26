import pandas as pd, re, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = r"G:\My Drive\ANTIGRAVITY\maramis"
ING = os.path.join(BASE, "1 - ingested")
OUT = os.path.join(BASE, "2 - analysis")
IMG = os.path.join(OUT, "images")
os.makedirs(IMG, exist_ok=True)

ev = pd.read_csv(os.path.join(ING, "events.csv"), encoding="utf-8-sig")
rooms = pd.read_csv(os.path.join(ING, "daftar_ruangan.csv"))
ev["start"] = pd.to_datetime(ev.start_date)
ev["end"] = pd.to_datetime(ev.end_date)
TODAY = pd.Timestamp("2026-09-26")
ev["status"] = ev.start.apply(lambda d: "Terlaksana" if d <= TODAY else "Pipeline")
core = ev[ev.is_loading_setup == 0]

R = {}
R["total_events"] = len(ev)
R["total_days"] = int(ev.duration_days.sum())
R["core_events"] = len(core)
R["loading_events"] = int(ev.is_loading_setup.sum())
R["loading_days"] = int(ev[ev.is_loading_setup == 1].duration_days.sum())
R["by_status"] = ev.groupby("status").size().to_dict()
R["unique_orgs"] = ev.organizer_name.nunique()

# unique calendar days occupied (union of date ranges)
days = set()
for _, r in ev.iterrows():
    for d in pd.date_range(r.start, r.end):
        days.add(d.normalize())
days = pd.Series(sorted(days))
R["unique_calendar_days"] = len(days)
# realised window Sep 29 2025 - Sep 26 2026
win = days[(days >= "2025-09-26") & (days <= TODAY)]
R["unique_days_last12m"] = len(win)
R["occupancy_rate_last12m_pct"] = round(len(win) / 366 * 100, 1)

# day-of-week of core events (start)
dow_names = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
dow = core.start.dt.dayofweek.value_counts().reindex(range(7), fill_value=0)
R["dow_core"] = {dow_names[i]: int(v) for i, v in dow.items()}
R["weekend_share_core_pct"] = round(dow[[5,6]].sum() / dow.sum() * 100, 1)

# monthly (core events and occupied days incl loading)
ev["ym"] = ev.start.dt.to_period("M")
monthly = ev.groupby("ym").agg(events=("event_id","count"), days=("duration_days","sum"))
monthly_core = core.groupby(core.start.dt.to_period("M")).size()
monthly["core"] = monthly_core
monthly = monthly.fillna(0).astype(int)
allm = pd.period_range("2025-09", "2026-12", freq="M")
monthly = monthly.reindex(allm, fill_value=0)
R["monthly"] = {str(k): v for k, v in monthly.to_dict("index").items()}

# sector grouping (macro)
def macro(s):
    if "Internal" in s: return "Kemenkeu (internal)"
    if s.startswith("Kementerian & Lembaga") or s.startswith("BUMN") or s.startswith("Lembaga Riset"): return "K/L, BUMN & lembaga"
    if any(k in s for k in ["Swasta","Festival","Industri Kreatif"]): return "Komersial & kreatif"
    if any(k in s for k in ["Komunitas","Pendidikan","Seni"]): return "Komunitas, pendidikan & seni"
    return "Lainnya / tidak teridentifikasi"
ev["macro"] = ev.organizer_sector.apply(macro)
core = ev[ev.is_loading_setup == 0]
ms = core.groupby("macro").agg(events=("event_id","count"), days=("duration_days","sum")).sort_values("events", ascending=False)
R["macro_sector_core"] = ms.to_dict("index")
cat = core.groupby("event_category").agg(events=("event_id","count"), days=("duration_days","sum")).sort_values("events", ascending=False)
R["category_core"] = cat.to_dict("index")

# repeat clients
oc = core[core.organizer_name != "Mitra Eksternal / Penyelenggara Umum"].groupby("organizer_name").size()
R["orgs_core_identified"] = len(oc)
R["repeat_orgs"] = int((oc >= 2).sum())
R["repeat_share_events_pct"] = round(oc[oc >= 2].sum() / oc.sum() * 100, 1)
R["top_repeat"] = oc.sort_values(ascending=False).head(10).to_dict()

# by building/floor
bf = core.groupby(["building","floor"]).size().sort_values(ascending=False)
R["building_floor_core"] = {f"{a} | {b}": int(v) for (a, b), v in bf.items()}

# room-code demand
codes = []
for c in core.room_codes.dropna():
    for x in re.split(r"[,;]\s*", str(c)):
        x = x.strip().replace("C.2.", "C2.").replace("A.2.", "A2.")
        if x and x != "-": codes.append(x)
R["room_code_mentions"] = pd.Series(codes).value_counts().to_dict()
# named rooms referenced via venue name
named = {}
for v in core.venue_name:
    for n in ["Majapahit","Bone","Sriwijaya","Kutai","Ternate","Mataram"]:
        if n in v: named[n] = named.get(n, 0) + 1
R["named_room_mentions"] = named
R["share_unspecified_venue_pct"] = round((core.floor.isin(["Unspecified"])).mean() * 100, 1)

# inventory
rooms_rent = rooms[rooms.skema == "Per Ruangan"].copy()
rooms_rent["kap"] = rooms_rent.kapasitas.astype(int)
R["inventory"] = {
    "rooms_total_listed": len(rooms),
    "rooms_per_ruangan": len(rooms_rent),
    "capacity_sum_per_ruangan": int(rooms_rent.kap.sum()),
    "tarif_min": int(rooms_rent.tarif_idr.min()), "tarif_max": int(rooms_rent.tarif_idr.max()),
    "tarif_median": int(rooms_rent.tarif_idr.median()),
    "sum_daily_rate_all_rooms": int(rooms_rent.tarif_idr.sum()),
    "rate_per_pax_median": int((rooms_rent.tarif_idr / rooms_rent.kap).median()),
    "named_rooms": rooms[rooms.nama != "-"][["kode","nama"]].values.tolist(),
    "unnamed_rooms": int((rooms.nama == "-").sum()),
    "by_floor": rooms_rent.groupby(["gedung","lantai"]).agg(n=("kode","count"), kap=("kap","sum"), tarif=("tarif_idr","sum")).reset_index().to_dict("records"),
}

# 2025 Q4 vs 2026 comparable months (Oct-Dec)
q = ev[ev.start.dt.month.isin([10,11,12])]
R["q4_compare"] = q.groupby(ev.start.dt.year).agg(events=("event_id","count"), days=("duration_days","sum")).to_dict("index")
# heritage walk counts
hw = core[core.event_category == "Heritage Walking Tour & Visit"]
R["heritage_walks"] = {"n": len(hw), "weekend_pct": round(hw.start.dt.dayofweek.isin([5,6]).mean()*100,1),
                       "orgs": hw.organizer_name.value_counts().to_dict()}
# longest events
R["long_events"] = core.sort_values("duration_days", ascending=False).head(8)[["clean_title","start_date","duration_days","organizer_name"]].values.tolist()

with open(os.path.join(OUT, "_analysis_output.json"), "w", encoding="utf-8") as f:
    json.dump(R, f, ensure_ascii=False, indent=1, default=str)

# ---------------- charts ----------------
BRICK, BAMBOO, PURPLE, WOOD, CHALK = "#9c3738", "#d8aa68", "#473538", "#8a400f", "#e2d6be"
INK, MUTED, GRID = "#2b2224", "#6b5f60", "#e6e0da"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.edgecolor": GRID,
                     "axes.labelcolor": MUTED, "xtick.color": MUTED, "ytick.color": MUTED,
                     "axes.spines.top": False, "axes.spines.right": False, "axes.spines.left": False,
                     "figure.facecolor": "white", "axes.facecolor": "white"})

def title(ax, t, s=None):
    ax.set_title(t, loc="left", fontsize=13, color=INK, fontweight="bold", pad=22)
    if s: ax.text(0, 1.02, s, transform=ax.transAxes, fontsize=9, color=MUTED)

def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(IMG, name), dpi=180); plt.close(fig)

# 1 monthly core events: realized vs pipeline via same hue, pipeline lighter
fig, ax = plt.subplots(figsize=(9, 4))
labels = [p.strftime("%b\n%y") for p in allm]
vals = monthly.core.values
cols = [BRICK if p.to_timestamp() <= TODAY else BAMBOO for p in allm]
ax.bar(range(len(allm)), vals, color=cols, width=0.7, edgecolor="white", linewidth=2)
for i, v in enumerate(vals):
    ax.text(i, v + 0.3, str(v), ha="center", fontsize=8, color=INK)
ax.set_xticks(range(len(allm))); ax.set_xticklabels(labels, fontsize=8)
ax.yaxis.grid(True, color=GRID); ax.set_axisbelow(True); ax.set_yticks([])
title(ax, "Kegiatan inti per bulan (tanpa sesi loading)", "Merah bata = terlaksana s.d. 26 Sep 2026 · kuning bambu = pipeline terjadwal")
save(fig, "01_kegiatan_bulanan.png")

# 2 macro sector
fig, ax = plt.subplots(figsize=(8, 3.6))
s = ms.events.sort_values()
ax.barh(s.index, s.values, color=BRICK, height=0.6, edgecolor="white", linewidth=2)
tot = s.sum()
for i, v in enumerate(s.values):
    ax.text(v + 0.5, i, f"{v}  ({v/tot*100:.0f}%)", va="center", fontsize=9, color=INK)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
title(ax, "Siapa yang memakai gedung?", f"Jumlah kegiatan inti per kelompok penyelenggara (n={tot})")
save(fig, "02_sektor_penyelenggara.png")

# 3 category
fig, ax = plt.subplots(figsize=(8, 4.2))
c = cat.events.sort_values()
ax.barh(c.index, c.values, color=PURPLE, height=0.6, edgecolor="white", linewidth=2)
for i, (v, d) in enumerate(zip(c.values, cat.days.reindex(c.index).values)):
    ax.text(v + 0.4, i, f"{v} kegiatan · {d} hari", va="center", fontsize=9, color=INK)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
title(ax, "Jenis kegiatan", f"Kegiatan inti per kategori (n={c.sum()})")
save(fig, "03_kategori_kegiatan.png")

# 4 day of week
fig, ax = plt.subplots(figsize=(7, 3.4))
cols = [BRICK]*5 + [BAMBOO]*2
ax.bar(dow_names, dow.values, color=cols, width=0.65, edgecolor="white", linewidth=2)
for i, v in enumerate(dow.values):
    ax.text(i, v + 0.4, str(v), ha="center", fontsize=9, color=INK)
ax.set_yticks([])
title(ax, "Hari pelaksanaan kegiatan inti", f"Akhir pekan (kuning) = {R['weekend_share_core_pct']}% kegiatan")
save(fig, "04_hari_kegiatan.png")

# 5 heritage walk organizers
fig, ax = plt.subplots(figsize=(8, 3.6))
h = hw.organizer_name.value_counts().head(8).sort_values()
ax.barh(h.index, h.values, color=WOOD, height=0.6, edgecolor="white", linewidth=2)
for i, v in enumerate(h.values):
    ax.text(v + 0.1, i, str(v), va="center", fontsize=9, color=INK)
ax.set_xticks([]); ax.spines["bottom"].set_visible(False)
title(ax, "Penyelenggara walking tour & kunjungan", f"{len(hw)} kunjungan; {R['heritage_walks']['weekend_pct']}% di akhir pekan")
save(fig, "05_walking_tour.png")

print(json.dumps({k: R[k] for k in ["total_events","total_days","core_events","loading_events","loading_days","by_status","unique_orgs","unique_calendar_days","unique_days_last12m","occupancy_rate_last12m_pct","weekend_share_core_pct","dow_core","orgs_core_identified","repeat_orgs","repeat_share_events_pct","share_unspecified_venue_pct","q4_compare"]}, ensure_ascii=False, indent=1, default=str))
print(ms); print(cat); print(R["room_code_mentions"]); print(R["named_room_mentions"]); print(R["inventory"]); print(R["top_repeat"]); print(R["heritage_walks"]); print(R["long_events"]); print(monthly.T)
