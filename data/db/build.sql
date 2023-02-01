CREATE TABLE IF NOT EXISTS Servers(
    server_id int NOT NULL UNIQUE,
    server_name text,
);

CREATE TABLE IF NOT EXISTS Users(
    user_id int NOT NULL UNIQUE,
);

CREATE TABLE IF NOT EXISTS user_in_server(
    server_id int NOT NULL,
    user_id int NOT NULL,
    is_in_server bit DEFAULT 1,
    FOREIGN KEY (server_id) REFERENCES Servers(server_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    UNIQUE(server_id, user_id)
);

CREATE TABLE IF NOT EXISTS Channels(
    server_id int NOT NULL,
    channel_id int NOT NULL UNIQUE,
    FOREIGN KEY (server_id) REFERENCES Servers(server_id)
);