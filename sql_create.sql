CREATE TABLE IF NOT EXISTS Singer (
	id_singer SERIAL PRIMARY KEY UNIQUE,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Album (
	id_album SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	yaer_of_release INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Track (
	id_track SERIAL PRIMARY KEY,
	id_album INTEGER NOT NULL REFERENCES Album(id_album),
	title_track VARCHAR(60) NOT NULL,
	duration INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
	id_genre SERIAL PRIMARY KEY UNIQUE,
	genre VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Collection (
	id_collection SERIAL PRIMARY KEY,
	title VARCHAR(60) NOT NULL,
	yaer_of_release INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS SingerGenre (
	id_singer INTEGER REFERENCES Singer(id_singer),
	id_genre INTEGER REFERENCES Genre(id_genre),
	CONSTRAINT pk PRIMARY KEY (id_singer, id_genre)
);

CREATE TABLE IF NOT EXISTS SingerAlbum (
	id_singer INTEGER REFERENCES Singer(id_singer),
	id_album INTEGER REFERENCES Album(id_album),
	CONSTRAINT pk2 PRIMARY KEY (id_singer, id_album)
);

CREATE TABLE IF NOT EXISTS CollectionTrack (
	id_collection INTEGER REFERENCES Collection(id_collection),
	id_track INTEGER REFERENCES Track(id_track),
	CONSTRAINT pk3 PRIMARY KEY (id_collection, id_track)
);