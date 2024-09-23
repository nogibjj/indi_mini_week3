import unittest
from mylib.lib import (
    load_dataset,
    print_head,
    generate_summary_statistics,
    group_by,
    build_log_histogram,
    create_scatter,
    save_to_markdown,
)
import os


class TestMainFunctionality(unittest.TestCase):
    def setUp(self):
        # Path to the example dataset (replace with the correct path if needed)
        self.dataset_path = "player_overview.csv"
        self.dataframe = load_dataset(self.dataset_path)

    def test_load_dataset(self):
        # Test that the dataset is loaded correctly
        self.assertIsNotNone(self.dataframe)
        self.assertGreater(len(self.dataframe), 0)

    def test_print_head(self):
        # Test that printing the head of the dataset works
        head = print_head(self.dataframe, n=5)
        self.assertEqual(len(head), 5)

    def test_generate_summary_statistics(self):
        # Test that summary statistics are generated correctly
        summary_stats = generate_summary_statistics(self.dataframe)
        self.assertIsNotNone(summary_stats)
        # Check that the summary contains statistics for numeric columns
        self.assertIn("Goals", summary_stats.columns)
        self.assertIn("Assists", summary_stats.columns)

    def test_group_by(self):
        # Test grouping by 'Position' and 'Nationality'
        position_counts = group_by(self.dataframe, "Position")
        self.assertIsNotNone(position_counts)

        nationality_counts = group_by(self.dataframe, "Nationality")
        self.assertIsNotNone(nationality_counts)

    def test_build_log_histogram(self):
        # Test that the histogram is generated and saved
        output_file = "test_goals_log_histogram.png"
        build_log_histogram(self.dataframe, "Goals", output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)  # Clean up the test file

    def test_create_scatter(self):
        # Test that the scatter plot is generated and saved
        output_file = "test_goals_assists_scatter.png"
        create_scatter(self.dataframe, "Goals", "Assists", output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)  # Clean up the test file

    def test_save_to_markdown(self):
        # Test saving summary statistics to a markdown file
        summary_stats = generate_summary_statistics(self.dataframe)
        output_file = "test_player_summary.md"
        save_to_markdown(summary_stats, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)  # Clean up the test file


if __name__ == "__main__":
    unittest.main()
