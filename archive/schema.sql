DROP TABLE IF EXISTS scenario_votes;
DROP TABLE IF EXISTS scenarios;
DROP TABLE IF EXISTS voters;

CREATE TABLE voters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    net_id TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    pgyear INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scenarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    panel TEXT NOT NULL,
    scenario_id TEXT NOT NULL,
    scenario_text TEXT NOT NULL,
    scenario_url TEXT NOT NULL,
    sex TEXT NOT NULL,
    age TEXT NOT NULL,
    body_area TEXT NOT NULL,
    priority_clinical_areas TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE scenario_votes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    vote TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(id),
    FOREIGN KEY (user_id) REFERENCES voters(id),
    UNIQUE(scenario_id, user_id)
);
