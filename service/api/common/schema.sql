--V38
--First ENUMs

CREATE TABLE 'Title' (
	'id'				INTEGER NOT NULL,
	'name'				TEXT NOT NULL,
	'synopsis'			TEXT NOT NULL,
	'start_date'		DATE NULL,
	'end_date'			DATE NULL,
	'chapter_count'		INTEGER NULL,
	'volume_count'		INTEGER NULL,
	PRIMARY KEY('id' AUTOINCREMENT)
);

CREATE TABLE 'Volume' (
	'id'				INTEGER NOT NULL,
	'title_id'			INTEGER NOT NULL,
	'index'				INTEGER NOT NULL,
	'name'				TEXT NULL,
	'synopsis'			TEXT NULL,
	'chapter_start'		INTEGER NULL,
	'chapter_end'		INTEGER NULL,
	'language'			INTEGER NOT NULL,
	'publisher'			INTEGER NOT NULL,
	'pages'				INTEGER NULL,
	'price'				INTEGER NULL,
	'released'			DATE NULL,
	'isbn-10'			INTEGER NULL,
	'isbn-13'			INTEGER NULL,
	PRIMARY KEY('id' AUTOINCREMENT),
	FOREIGN KEY('title_id') REFERENCES 'Title'('id')
);
