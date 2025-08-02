import sqlite3
s=sqlite3.connect("sqlite.db")
s.execute("""
CREATE TABLE IF NOT EXISTS student (
    st_id   INTEGER PRIMARY KEY AUTOINCREMENT,  -- auto‑incrementing key
    st_name TEXT,
    st_class TEXT,
    st_email TEXT
)
""")
s.commit()
s.close()