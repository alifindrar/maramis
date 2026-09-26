# Gedung A.A. Maramis Event Database (2025–2026)

This directory contains the ingested, structured historical event database of Gedung A.A. Maramis from the official Teamup Calendar feed (`https://teamup.com/ksmwq7sm1fck44ynrs`).

## 📦 Available Artifacts

| File | Format | Description |
| :--- | :--- | :--- |
| [`events.sqlite`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events.sqlite) | SQLite 3 | Relational database containing normalized `events` table, `venues` catalog, and analytical views (`v_events_summary`, `v_monthly_stats`, `v_venue_utilization`, `v_organizer_rankings`, `v_category_stats`). |
| [`events.csv`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events.csv) | CSV | Master tabular dataset with all enriched fields (clean title, room codes, building, floor, venue, organizer, sector, category, dates, duration). |
| [`events.xlsx`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events.xlsx) | Excel Workbook | Formatted multi-sheet workbook including KPI summary, master events table, monthly breakdown, venue utilization, category breakdown, and organizer rankings. |
| [`events.json`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events.json) | JSON | Standardized structured JSON array of all 172 events with full parsed attributes. |
| [`events_raw.json`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events_raw.json) | JSON | Raw API response from Teamup for archival and audit integrity. |
| [`teamup_calendar.ics`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/teamup_calendar.ics) | iCalendar (.ics) | Standard iCalendar feed downloaded directly from Teamup server. |
| [`events_database.md`](file:///g:/My%20Drive/ANTIGRAVITY/maramis/1%20-%20ingested/events_database.md) | Markdown | Full chronological catalog and analytical report for 2025 and 2026. |

## 🗄️ Database Schema (`events.sqlite`)

```sql
CREATE TABLE events (
    event_id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    clean_title TEXT NOT NULL,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    duration_days INTEGER NOT NULL,
    is_all_day INTEGER NOT NULL,
    is_loading_setup INTEGER NOT NULL,
    event_category TEXT NOT NULL,
    building TEXT NOT NULL,
    floor TEXT NOT NULL,
    room_codes TEXT,
    venue_name TEXT NOT NULL,
    organizer_name TEXT NOT NULL,
    organizer_sector TEXT NOT NULL,
    pic_or_contact TEXT,
    notes_clean TEXT,
    notes_raw TEXT,
    location_field TEXT,
    who_field TEXT,
    subcalendar_id INTEGER,
    subcalendar_name TEXT,
    teamup_version TEXT,
    creation_dt TEXT,
    update_dt TEXT,
    source_url TEXT
);
```

## 💡 Example Queries

### 1. Monthly Utilization Overview (SQL)
```sql
SELECT * FROM v_monthly_stats;
```

### 2. Top Venues by Total Occupied Days
```sql
SELECT venue_name, booking_count, total_occupied_days FROM v_venue_utilization LIMIT 10;
```

### 3. Load with Pandas in Python
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('events.sqlite')
df = pd.read_sql_query('SELECT * FROM events', conn)
print(f'Total events: {len(df)}')
```