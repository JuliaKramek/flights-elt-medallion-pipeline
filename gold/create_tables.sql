CREATE TABLE IF NOT EXISTS FLIGHTS.GOLD.TRAVEL_GOLD (
    ticketing_airline VARCHAR,
    origin VARCHAR,
    destination VARCHAR,
    cabin VARCHAR,
    total_transactions NUMBER
);

MERGE INTO FLIGHTS.GOLD.TRAVEL_GOLD t
USING (
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
        f.cabin
) s
ON t.ticketing_airline = s.ticketing_airline
AND t.origin = s.origin
AND t.destination = s.destination
AND t.cabin = s.cabin

WHEN MATCHED THEN UPDATE SET
    total_transactions = s.total_transactions

WHEN NOT MATCHED THEN INSERT (
    ticketing_airline,
    origin,
    destination,
    cabin,
    total_transactions
)
VALUES (
    s.ticketing_airline,
    s.origin,
    s.destination,
    s.cabin,
    s.total_transactions
);
