"""Print saved reservations: python view_reservations.py   (add --csv for CSV output)"""
import csv, os, sqlite3, sys
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "ghazal.db")
if not os.path.exists(p):
    sys.exit("No reservations yet.")
rows = sqlite3.connect(p).execute(
    "SELECT id,created_at,name,phone,email,date,time,guests,notes FROM reservations ORDER BY date,time").fetchall()
if "--csv" in sys.argv:
    w = csv.writer(sys.stdout); w.writerow(["id","received","name","phone","email","date","time","guests","notes"]); w.writerows(rows)
else:
    for r in rows:
        print(f"#{r[0]} {r[5]} {r[6]} | {r[7]} guests | {r[2]} | {r[3]} | {r[4] or '-'} | {r[8] or '-'} (received {r[1]})")
    print(f"{len(rows)} reservation(s)")
