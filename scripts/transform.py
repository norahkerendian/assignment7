from pathlib import Path
import pandas as pd

INPUT_PATH = Path("data/clean/events.csv")
OUTPUT_PATH = Path("data/transformed/events.csv")


def main():
    # Load cleaned data
    df = pd.read_csv(INPUT_PATH)

    # Ensure timestamp is parsed correctly
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Add date column (YYYY-MM-DD)
    df["date"] = df["timestamp"].dt.strftime("%Y-%m-%d")

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save transformed data
    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()
