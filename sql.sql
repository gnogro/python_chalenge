CREATE TABLE clients (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    celphone VARCHAR(15) NOT NULL,
    status BOOLEAN NOT NULL,
    hash VARCHAR(64) NOT NULL,
    list_id VARCHAR(64) NOT NULL
);