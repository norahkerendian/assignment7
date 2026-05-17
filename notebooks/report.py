import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("../data/features/events.csv")
    return (df,)


@app.cell
def _(df, plt):
    fig, ax = plt.subplots()

    ax.hist(df["duration_minutes"], bins=20)
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Minutes")
    ax.set_ylabel("Frequency")

    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
