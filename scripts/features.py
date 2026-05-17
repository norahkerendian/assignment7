from pathlib import Path
import pandas as pd

INPUT_PATH = Path("data/transformed/events.csv")
OUTPUT_PATH = Path("data/features/events.csv")


def main():
    # Load transformed data
    df = pd.read_csv(INPUT_PATH)

    # 1. duration in minutes
    df["duration_minutes"] = df["duration_seconds"] / 60

    # 2. weekday from date
    df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save final dataset
    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()
