import sqlite3
import csv
import os

# Show current working directory
print("Looking for file in:", os.getcwd())

# Connect to SQLite database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# Drop old tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# Open and read CSV file
try:
    with open('tracks.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header
        rows = list(reader)
        print(f"Total rows found: {len(rows)}")

        for row in rows:
            if len(row) < 7:
                continue

            name = row[0]      # Track title
            artist = row[1]    # Artist
            album = row[2]     # Album
            count = row[3]     # Count
            rating = row[4]    # Rating
            length = row[5]    # Length
            genre = row[6]     # Genre


            if not (name and artist and album and genre):
                continue

            # Insert artist
            cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)', (artist,))
            cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
            artist_id = cur.fetchone()[0]

            # Insert genre
            cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)', (genre,))
            cur.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
            genre_id = cur.fetchone()[0]

            # Insert album
            cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)', (album, artist_id))
            cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
            album_id = cur.fetchone()[0]

            # Insert track
            cur.execute('''
                INSERT OR REPLACE INTO Track
                (title, album_id, genre_id, len, rating, count)
                VALUES (?, ?, ?, ?, ?, ?)''',
                (name, album_id, genre_id, length, rating, count))

        conn.commit()
        print("Database successfully updated.")

        # Run verification query
        print("\nSample Query Result:")
        for row in cur.execute('''
            SELECT Track.title, Artist.name, Album.title, Genre.name 
            FROM Track 
            JOIN Genre ON Track.genre_id = Genre.id
            JOIN Album ON Track.album_id = Album.id
            JOIN Artist ON Album.artist_id = Artist.id
            ORDER BY Artist.name 
            LIMIT 3
        '''):
            print(row)

except FileNotFoundError:
    print("Error: 'tracks.csv' not found in this directory.")

finally:
    conn.close()
