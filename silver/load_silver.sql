-- DIM AIRLINE
INSERT INTO silver.dim_airline
SELECT DISTINCT
    ticketing_airline,
    marketing_airline
FROM bronze.travel_raw
WHERE ticketing_airline IS NOT NULL;

-- DIM ROUTE
INSERT INTO silver.dim_route
SELECT DISTINCT
    origin,
    destination,
    country
FROM bronze.travel_raw;

-- FACT TRAVEL
INSERT INTO silver.fact_travel
SELECT
    gen_random_uuid(),  -- zamiast UUID_STRING()

    transaction_key,

    NULL,
    NULL,

    cabin,
    agency,

    NULLIF(NULLIF(departure_date, '\N'), '')::DATE,
    NULLIF(NULLIF(issue_date, '\N'), '')::DATE,

    flight_number,

    NULLIF(NULLIF(seg_number, '\N'), '')::INT

FROM bronze.travel_raw;
