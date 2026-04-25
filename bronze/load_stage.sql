COPY bronze.travel_raw
FROM '/tmp/travel.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ',',
    QUOTE '"'
);
