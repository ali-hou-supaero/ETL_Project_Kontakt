-- AirLife Database Setup
-- Run this script to create the necessary tables for the ETL pipeline

-- Drop tables if they exist (for clean restart)
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS airports;

-- Airports table - stores airport information from CSV data
CREATE TABLE airports (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    city VARCHAR(100),
    country VARCHAR(100),
    iata_code VARCHAR(3),
    icao_code VARCHAR(4),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    altitude INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Flights table - stores current flight information from API
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(6) NOT NULL,
    callsign VARCHAR(10),
    origin_country VARCHAR(50),
    time_position BIGINT,
    last_contact BIGINT,
    longitude DECIMAL(10,6),
    latitude DECIMAL(10,6),
    altitude DECIMAL(8,2), -- in feet, converted from meters
    on_ground BOOLEAN,
    velocity DECIMAL(8,2),
    true_track DECIMAL(6,2),
    vertical_rate DECIMAL(8,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better query performance
CREATE INDEX idx_airports_iata ON airports(iata_code);
CREATE INDEX idx_airports_country ON airports(country);
CREATE INDEX idx_flights_icao24 ON flights(icao24);
CREATE INDEX idx_flights_country ON flights(origin_country);

-- Verify tables were created
\dt

SELECT 'Database setup complete!' as status;
