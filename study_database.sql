
DROP TABLE IF EXISTS groups;
CREATE table groups(
	id integer primary key autoincrement,
	group_name varchar(255) not null
);


DROP TABLE IF EXISTS students;
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	student_name VARCHAR(255) NOT NULL,
	group_id INTEGER not null,
	FOREIGN KEY (group_id) REFERENCES groups (id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS professors;
CREATE table professors(
	id integer primary key autoincrement,
	profesor_name varchar (255) not null
);

DROP TABLE IF EXISTS lesons;
CREATE table lesons(
	id integer primary key autoincrement,
	leson_name varchar(255) not null,
	id_profesor integer not null,
	FOREIGN KEY (id_profesor) REFERENCES professors (id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);

DROP TABLE IF EXISTS graduates;
CREATE table graduates(
	id integer primary key autoincrement,
	grade integer not null,
	date_of date not null,
	student_id integer,
	leson_id integer,
	FOREIGN KEY (student_id) REFERENCES students (id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
    FOREIGN KEY (leson_id) REFERENCES lesons (id)
		ON DELETE SET NULL
        ON UPDATE CASCADE
);