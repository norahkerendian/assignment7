from pathlib import Path
import pandas as pd

# Valid event types (adjust only if your class specifies different ones)
VALID_EVENT_TYPES = {"click", "view", "purchase", "login", "logout"}

INPUT_PATH = Path("data/raw/events.csv")
OUTPUT_PATH = Path("data/clean/events.csv")


def main():
    # Load data
    df = pd.read_csv(INPUT_PATH)

    # 1. Drop rows with ANY missing fields
    df = df.dropna()

    # 2. Validate event_type
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # 3. Ensure duration_seconds is numeric and positive
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # 4. Normalize timestamp to ISO 8601
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df = df.dropna(subset=["timestamp"])
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    # df['duration_seconds'] = int(df['duration_seconds'])

    # Ensure output directory exists
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned data
    df.to_csv(OUTPUT_PATH, index=False)


if __name__ == "__main__":
    main()

