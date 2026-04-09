def run_bronze():
    print("Running BRONZE layer")

    steps = [
        "create_schema.sql",
        "create_stage.sql",
        "create_stage_table.sql",
        "load_stage.sql",
        "create_tables.sql",
        "load_bronze.sql"
    ]

    for step in steps:
        print(f"Executing bronze/{step}")

    print("BRONZE finished\n")