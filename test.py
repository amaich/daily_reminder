import psycopg2
import db

conn = psycopg2.connect("dbname=reminder_app user=postgres password=qwerty123 host=ovz3.j90259871.0n03n.vps.myjino.ru port=49321") # 9010
cursor = conn.cursor()

db.ins(conn, cursor, '174238692', 'test', '16:39')
for i in db.sel(cursor):
        print(i)



for i in db.sel(cursor):
        print(i)


cursor.close()
conn.close()
