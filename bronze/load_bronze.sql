INSERT INTO bronze.travel_raw
SELECT *,
CURRENT_TIMESTAMP(),
UUID_STRING()
FROM bronze.stage_travel;
