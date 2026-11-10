"""Print newsletter subscribers: python view_subscribers.py   (add --csv for a spreadsheet file)"""
import csv, os, sqlite3, sys
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ghazal.db")
if not os.path.exists(p):
    sys.exit("No subscribers yet.")
try:
    rows = sqlite3.connect(p).execute("SELECT email,lang,created_at FROM subscribers ORDER BY id").fetchall()
except sqlite3.OperationalError:
    sys.exit("No subscribers yet.")
if "--csv" in sys.argv:
    w = csv.writer(sys.stdout); w.writerow(["email", "language", "subscribed_at"]); w.writerows(rows)
else:
    for r in rows:
        print(f"{r[0]} ({r[1]}) {r[2]}")
    print(f"{len(rows)} subscriber(s)")