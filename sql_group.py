import sqlalchemy as sq
from pprint import pprint

db = 'postgresql+psycopg2://admin_shop:28012011@localhost/music_shop'
engine = sq.create_engine(db)
connection = engine.connect()
print(engine)

sel = connection.execute("""
SELECT genre.genre, COUNT(id_singer) FROM SingerGenre
LEFT JOIN genre ON SingerGenre.id_genre = Genre.id_genre
GROUP BY genre.genre;
""").fetchall()
pprint(sel)

sel1 = connection.execute("""
SELECT COUNT(id_track) FROM Track
LEFT JOIN Album ON Track.id_album = Album.id_album
WHERE Album.yaer_of_release BETWEEN 2019 AND 2020;
""").fetchall()
pprint(sel1)

sel2 = connection.execute("""
SELECT album.title, AVG(track.duration) FROM track
LEFT JOIN Album ON Track.id_album = Album.id_album
GROUP BY album.title
ORDER BY AVG(Track.duration);
""").fetchall()
pprint(sel2)

sel3 = connection.execute("""
SELECT DISTINCT(singer.name) FROM Album
LEFT JOIN SingerAlbum ON Album.id_album = SingerAlbum.id_album 
LEFT JOIN Singer ON SingerAlbum.id_singer = Singer.id_singer
WHERE Album.yaer_of_release != 2020;
""").fetchall()
pprint(sel3)

sel4 = connection.execute("""
SELECT DISTINCT(Collection.title) FROM Singer
LEFT JOIN SingerAlbum ON Singer.id_singer = SingerAlbum.id_singer 
LEFT JOIN Album ON SingerAlbum.id_album = Album.id_album 
LEFT JOIN Track ON Track.id_album = Album.id_album 
LEFT JOIN CollectionTrack ON Track.id_track = CollectionTrack.id_track 
LEFT JOIN collection ON CollectionTrack.id_collection = Collection.id_collection
WHERE singer.name = 'Niletto' AND CollectionTrack.id_collection IS NOT NULL;
""").fetchall()
pprint(sel4)

sel5 = connection.execute("""
SELECT album.title FROM Album
Left JOIN SingerAlbum ON Album.id_album = SingerAlbum.id_album
LEFT JOIN Singer ON SingerAlbum.id_singer = Singer.id_singer
LEFT JOIN SingerGenre ON Singer.id_singer = SingerGenre.id_singer
LEFT JOIN Genre ON SingerGenre.id_genre = Genre.id_genre
GROUP BY Album.title
HAVING COUNT(DISTINCT Genre.genre) > 1;
""").fetchall()
pprint(sel5)

sel6 = connection.execute("""
SELECT track.title_track FROM Track
LEFT JOIN CollectionTrack ON track.id_track = CollectionTrack.id_track 
WHERE CollectionTrack.id_collection is NULL;
""").fetchall()
pprint(sel6)

sel7 = connection.execute("""
SELECT Singer.name, track.duration  FROM Singer
LEFT JOIN SingerAlbum ON Singer.id_singer = SingerAlbum.id_singer
LEFT JOIN Album ON SingerAlbum.id_album = Album.id_album
LEFT JOIN Track ON Album.id_album = Track.id_album
GROUP BY Singer.name, Track.duration
HAVING Track.duration = (SELECT MIN(Track.duration) FROM Track);
""").fetchall()
pprint(sel7)

sel8 = connection.execute("""
SELECT DISTINCT(Album.title), COUNT(Track.id_track) FROM Album
LEFT JOIN Track ON Album.id_album = Track.id_album
GROUP BY Album.title;
""").fetchall()
pprint(sel8)