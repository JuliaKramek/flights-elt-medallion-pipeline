DROP TABLE IF EXISTS gold.travel_gold;

CREATE TABLE gold.travel_gold AS
SELECT
    a.ticketing_airline,
    r.origin,
    r.destination,
    f.cabin,
    COUNT(*) AS total_transactions
FROM silver.fact_travel f
JOIN silver.dim_airline a
    ON f.airline_id = a.airline_id
JOIN silver.dim_route r
    ON f.route_id = r.route_id
GROUP BY
    a.ticketing_airline,
    r.origin,
    r.destination,
    f.cabin;
