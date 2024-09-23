"""
Main file to apply the functions defined in lib.py.
This script loads a dataset, applies statistical functions, and generates visualizations for soccer player data.
"""

from mylib.lib import (
    load_dataset,
    print_head,
    generate_summary_statistics,
    group_by,
    build_log_histogram,
    create_scatter,  # Added the create_scatter function import
    save_to_markdown,
)

# Path to dataset
dataset_path = "player_overview.csv"


def main():
    """
    Main function to load dataset, perform analysis, and save results.
    """
    dataframe = load_dataset(dataset_path)

    if dataframe is not None:
        # Print the head of the dataset
        print("Displaying the first few rows of the dataset:")
        print_head(dataframe)

        # Generate and print summary statistics
        print("\nGenerating summary statistics:")
        summary_stats = generate_summary_statistics(dataframe)
        print(summary_stats)

        # Group by 'Position' and 'Nationality' columns and display results
        print("\nValue counts for 'Position':")
        print(group_by(dataframe, "Position"))

        print("\nValue counts for 'Nationality':")
        print(group_by(dataframe, "Nationality"))

        # Build and save histogram for 'Goals'
        print("\nGenerating and saving a logarithmic histogram for 'Goals':")
        build_log_histogram(dataframe, "Goals", "goals_log_histogram.png")

        # Create and save scatter plot for 'Goals' and 'Assists'
        print("\nGenerating and saving a scatter plot for 'Goals' and 'Assists':")
        create_scatter(dataframe, ["Goals", "Assists"], "goals_assists_scatter.png")

        # Save the summary statistics to markdown
        print("\nSaving summary statistics to markdown file:")
        save_to_markdown(summary_stats, "player_summary.md")
    else:
        print("Dataset was not successfully loaded")


if __name__ == "__main__":
    main()
