"""
Library file that lists all the necessary functions for soccer player data analysis.
"""

import polars as pl
import matplotlib.pyplot as plt


# Load dataset from csv file using Polars
def load_dataset(dataset_path):
    df = pl.read_csv(dataset_path)
    return df


# Print the head of the dataset
def print_head(df, n=5):
    data_head = df.head(n)
    print(data_head)
    return data_head


# Grab the mean of a column
def grab_mean(df, col):
    return df.select(pl.col(col).mean()).item()


# Grab the median of a column
def grab_median(df, col):
    return df.select(pl.col(col).median()).item()


# Grab the standard deviation of a column
def grab_std(df, col):
    return df.select(pl.col(col).std()).item()


# Grab the max of a column
def grab_max(df, col):
    return df.select(pl.col(col).max()).item()


# Generate descriptive statistics: mean, median, std for numeric columns
def generate_summary_statistics(df):
    """
    Generates summary statistics (mean, median, std) for numeric columns in the dataframe.

    :param df: Polars DataFrame
    :return: Polars DataFrame with summary statistics
    """
    summary_stats = df.select(
        [
            pl.col(column).mean().alias(f"{column}_mean")
            for column, dtype in df.schema.items()
            if dtype in [pl.Float64, pl.Int64]
        ]
        + [
            pl.col(column).median().alias(f"{column}_median")
            for column, dtype in df.schema.items()
            if dtype in [pl.Float64, pl.Int64]
        ]
        + [
            pl.col(column).std().alias(f"{column}_std")
            for column, dtype in df.schema.items()
            if dtype in [pl.Float64, pl.Int64]
        ]
    )
    return summary_stats


# Group by a categorical column and count occurrences
def group_by(df, column_name):
    return df.select(pl.col(column_name).value_counts())


# Create a logarithmic histogram for a given numeric column
def build_log_histogram(df, column_name, output_file):
    column_data = df[column_name].to_numpy()

    # Create the histogram with a logarithmic scale on the y-axis
    plt.hist(column_data, bins=10, edgecolor="white", log=True)

    # Set labels and title
    plt.xlabel(column_name)
    plt.ylabel("Frequency (Log Scale)")
    plt.title(f"{column_name} Logarithmic Histogram")

    # Save the plot to a file
    plt.savefig(output_file)
    plt.show()


# Create a scatter plot for multiple columns
def create_scatter(df, columns, output_file="scatter.png"):
    """
    Creates and saves a scatterplot for the specified columns.

    :param df: Polars DataFrame
    :param columns: list of str, column names for scatterplot
    :param output_file: str, file path to save the scatterplot
    """
    colors = ["red", "green", "yellow", "blue"]
    for i, column in enumerate(columns):
        plt.scatter(
            df["age"].to_numpy(),
            df[column].to_numpy(),
            label=column,
            color=colors[i % len(colors)],
        )
    plt.xlabel("Age")
    plt.ylabel("Value")
    plt.title(f"Scatterplot of {', '.join(columns)}")
    plt.legend()
    plt.savefig(output_file)
    plt.show()


# Save summary statistics to markdown
def save_to_markdown(summary_stats, output_file):
    markdown_table = str(summary_stats)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("# Summary Statistics\n")
        file.write(markdown_table)
