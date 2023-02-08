CREATE TABLE IF NOT EXISTS Servers(
    server_id int PRIMARY KEY,
    server_name text
);

CREATE TABLE IF NOT EXISTS Users(
    user_id int PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS user_in_server(
    server_id int NOT NULL,
    user_id int NOT NULL,
    is_in_server bit DEFAULT 1,
    FOREIGN KEY (server_id) REFERENCES Servers(server_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    PRIMARY KEY(server_id, user_id)
);

CREATE TABLE IF NOT EXISTS Channels(
    channel_id int PRIMARY KEY,
    server_id int NOT NULL,
    FOREIGN KEY (server_id) REFERENCES Servers(server_id)
);

CREATE TABLE IF NOT EXISTS fursona_characters(
    character_id INTEGER PRIMARY KEY AUTOINCREMENT, -- incremental
    user_id int NOT NULL,
    character_name text DEFAULT 'No name',
    description text DEFAULT 'No description yet',
    favorited int,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS character_art(
    art_id INTEGER PRIMARY KEY AUTOINCREMENT, --incremental
    character_id int NOT NULL,
    description text,
    art_image blob NOT NULL, --binary encoded image format
    FOREIGN KEY (character_id) REFERENCES fursona_characters(character_id)
);

CREATE TABLE IF NOT EXISTS tester(
    description text
);