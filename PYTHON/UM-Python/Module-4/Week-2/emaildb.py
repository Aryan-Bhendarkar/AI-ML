import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Clear out the table if it already exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create a new table
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Open the mbox.txt file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

# Loop through each line in the file
for line in fh:
    if not line.startswith('From: '): 
        continue
    parts = line.split()
    email = parts[1]
    domain = email.split('@')[1]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

# Commit once, after processing all lines
conn.commit()

# Optional: print top 10 results
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
