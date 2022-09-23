CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(45),
    subtitle VARCHAR(45),
    body TEXT,
    created_on DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime'))
);

INSERT INTO notes(
    title,
    subtitle,
    body
) VALUES (
    "test",
    "test",
    "test"
);