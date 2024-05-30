-- Create the track_info table
CREATE TABLE song (
    id VARCHAR PRIMARY KEY,
    artist_name VARCHAR NOT NULL,
    artist_spotify_id VARCHAR NOT NULL,
    song_title VARCHAR NOT NULL,
    song_spotify_id VARCHAR NOT NULL,
    genre VARCHAR,
    bpm FLOAT NOT NULL,
    is_bpm_acceptable BOOLEAN NOT NULL
);

SELECT * FROM song;
SELECT * FROM song



