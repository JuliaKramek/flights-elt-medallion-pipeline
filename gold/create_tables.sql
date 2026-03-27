CREATE OR REPLACE TABLE FLIGHTS.GOLD.TRAVEL_GOLD AS
SELECT
a.ticketing_airline,
r.origin,
r.destination,
f.cabin,
COUNT(*) AS total_transactions
FROM FLIGHTS.SILVER.FACT_TRAVEL f
JOIN FLIGHTS.SILVER.AIRLINE a
ON f.airline_id = a.airline_id
JOIN FLIGHTS.SILVER.ROUTE r
ON f.route_id = r.route_id
GROUP BY
a.ticketing_airline,
r.origin,
r.destination,
f.cabin;
