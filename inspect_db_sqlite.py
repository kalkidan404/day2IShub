import sqlite3

conn = sqlite3.connect('chroma_db/chroma.sqlite3')
c = conn.cursor()

# show tables
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print('tables', c.fetchall())

# inspect documents table
try:
    c.execute('SELECT * FROM documents')
    rows = c.fetchall()
    print('documents rows', len(rows))
    for r in rows:
        print(r)
except Exception as e:
    print('error reading documents table', e)

conn.close()
