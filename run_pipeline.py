from bronze import run_bronze
from silver import run_silver
from gold import run_gold


def run_pipeline():
    print("\nStarting pipeline\n")

    run_bronze()
    run_silver()
    run_gold()

    print("\nPipeline finished\n")


if __name__ == "__main__":
    run_pipeline()