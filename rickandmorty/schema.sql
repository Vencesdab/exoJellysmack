DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS episodes;
DROP TABLE IF EXISTS joinEpisodesCharacters;

CREATE TABLE characters (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  status TEXT NOT NULL,
  species TEXT NOT NULL,
  type TEXT,
  gender TEXT NOT NULL
);

CREATE TABLE episodes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  air_date TEXT NOT NULL,
  episode TEXT NOT NULL
);

CREATE TABLE joinEpisodesCharacters (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  character_id INTEGER NOT NULL,
  episode_id INTEGER NOT NULL,
  FOREIGN KEY (character_id) REFERENCES characters(id),
  FOREIGN KEY (episode_id) REFERENCES episodes(id)
);

CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  comment TEXT NOT NULL,
  character_id INTEGER,
  episode_id INTEGER,
  FOREIGN KEY (character_id) REFERENCES characters(id),
  FOREIGN KEY (episode_id) REFERENCES episodes(id)
);