DROP TABLE IF EXISTS silver.dim_airline;
DROP TABLE IF EXISTS silver.dim_route;
DROP TABLE IF EXISTS silver.fact_travel;

CREATE TABLE silver.dim_airline (
    airline_id SERIAL PRIMARY KEY,
    ticketing_airline VARCHAR,
    marketing_airline VARCHAR
);

CREATE TABLE silver.dim_route (
    route_id SERIAL PRIMARY KEY,
    origin VARCHAR,
    destination VARCHAR,
    country VARCHAR
);

CREATE TABLE silver.fact_travel (
    event_id UUID DEFAULT gen_random_uuid(),
    transaction_key VARCHAR,
    airline_id INT,
    route_id INT,
    cabin VARCHAR,
    agency VARCHAR,
    departure_date DATE,
    issue_date DATE,
    flight_number VARCHAR,
    seg_number VARCHAR
);
