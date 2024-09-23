import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from csv file using Pandas
def load_dataset(dataset_path):
    return pd.read_csv(dataset_path)

# Print the head of the dataset
def print_head(df, n=5):
    data_head = df.head(n)
    print(data_head)
    return data_head

# Generate descriptive statistics for numeric columns
def generate_summary_statistics(df):
    return df.describe()

# Group by a categorical column and count occurrences
def group_by(df, column_name):
    return df[column_name].value_counts()

def build_log_histogram(df, column_name, output_file):
    plt.hist(
        df[column_name].dropna(), bins=10, log=True, edgecolor='white'
    )
    plt.xlabel(column_name)
    plt.ylabel('Frequency (Log Scale)')
    plt.title(f'{column_name} Logarithmic Histogram')
    plt.savefig(output_file)
    plt.show()  # Ensure this is present

def create_scatter(df, x_col, y_col, output_file="scatter.png"):
    plt.scatter(df[x_col], df[y_col], alpha=0.5)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Scatter Plot of {x_col} vs {y_col}')
    plt.savefig(output_file)
    plt.show()  # Ensure this is present

# Save summary statistics to markdown
def save_to_markdown(summary_stats, output_file):
    markdown_table = summary_stats.to_markdown()
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("# Summary Statistics\n")
        file.write(markdown_table)

