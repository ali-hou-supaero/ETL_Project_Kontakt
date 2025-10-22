-- AirLife Database Setup
-- Run this script to create the necessary tables for the ETL pipeline

-- Drop tables if they exist (for clean restart)
DROP TABLE IF EXISTS users;


-- Users table - stores user information from CSV data
CREATE TABLE users (
    user_id INTEGER NOT NULL,
    timestamp VARCHAR(200),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Verify tables were created
\dt

SELECT 'Database setup complete!' as status;
