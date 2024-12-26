CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) UNIQUE NOT NULL,
    last_name VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE meetings (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    description TEXT
);

CREATE TABLE meeting_participants (
    meeting_id INT REFERENCES meetings(id) ON DELETE CASCADE,
    person_id INT REFERENCES persons(id) ON DELETE CASCADE,
    PRIMARY KEY (meeting_id, person_id)
);
