SELECT * FROM playlists;

-- insert
INSERT INTO playlists
(PlaylistId, Name)
VALUES
(19, 'Genshin Impact'),
(20, 'Elder Ring');

SELECT * FROM playlists;

-- delete
DELETE FROM playlists
WHERE PlaylistId = 19 or PlaylistId = 20;

SELECT * FROM playlists;