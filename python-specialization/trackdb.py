import xml.etree.ElementTree as et
import _sqlite3

fname = input('Enter file song_title ')

conn = _sqlite3.connect('trackdb.sqlite')
curr = conn.cursor()

curr.execute('''DROP TABLE IF EXISTS Track''')
curr.execute('''DROP TABLE IF EXISTS Album''')
curr.execute('''DROP TABLE IF EXISTS Genre''')
curr.execute('''DROP TABLE IF EXISTS Artist''')

curr.execute('''CREATE TABLE Artist (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT UNIQUE)''')

curr.execute('''CREATE TABLE Genre (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name    TEXT UNIQUE)''')

curr.execute('''CREATE TABLE Album (
                id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                artist_id  INTEGER,
                title   TEXT UNIQUE)''')

curr.execute('''CREATE TABLE Track (
                id  INTEGER NOT NULL PRIMARY KEY 
                    AUTOINCREMENT UNIQUE,
                title TEXT  UNIQUE,
                album_id  INTEGER,
                genre_id  INTEGER,
                len INTEGER,
                rating INTEGER,
                count INTEGER)''')

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = et.parse(fname)
all = stuff.findall('dict/dict/dict')

for entry in all:
    if lookup(entry, 'Track ID') is None: continue

    track_title = lookup(entry,'Name')
    length = lookup(entry, 'Total Time')
    rating = lookup(entry, 'Rating')
    count = lookup(entry, 'Play Count')
    album_title = lookup(entry, 'Album')
    genre_name = lookup(entry, 'Genre')
    artist_name = lookup(entry, 'Artist')

    if track_title is None or artist_name is None or album_title is None:
        continue

    curr.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''',
                (artist_name,))
    curr.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name,))
    artist_id = curr.fetchone()[0]

    curr.execute('''INSERT OR IGNORE INTO Album (artist_id , title) VALUES ( ?, ? )''',
                 (artist_id,artist_name))
    curr.execute('''SELECT id FROM Artist WHERE name = ?''', (artist_name,))
    album_id = curr.fetchone()[0]

    curr.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''',
                 (genre_name,))
    curr.execute('''SELECT id FROM Genre WHERE name = ?''', (genre_name,))
    genre_id = curr.fetchone()[0]

    curr.execute('''INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,? )''',
                 (track_title, album_id, genre_id, length, rating, count))

    conn.commit()