import unittest
from mylib.lib import (
    load_dataset,
    grab_mean,
    grab_median,
    grab_max,
    grab_std,
    generate_summary_statistics,  # Added the import for generate_summary_statistics
    group_by,
    build_log_histogram,
    create_scatter,
)
import os


class TestLibFunctions(unittest.TestCase):
    def setUp(self):
        # Example dataset (replace with the correct path if needed)
        self.dataset_path = "player_overview.csv"
        self.dataframe = load_dataset(self.dataset_path)

    def test_load_dataset(self):
        # Test that the dataset is loaded correctly
        self.assertIsNotNone(self.dataframe)
        self.assertGreater(len(self.dataframe), 0)

    def test_grab_mean(self):
        # Test grabbing the mean of the "Goals" column
        mean_goals = grab_mean(self.dataframe, "Goals")
        self.assertIsInstance(mean_goals, float)

    def test_grab_median(self):
        # Test grabbing the median of the "Goals" column
        median_goals = grab_median(self.dataframe, "Goals")
        self.assertIsInstance(median_goals, float)

    def test_grab_std(self):
        # Test grabbing the standard deviation of the "Goals" column
        std_goals = grab_std(self.dataframe, "Goals")
        self.assertIsInstance(std_goals, float)

    def test_grab_max(self):
        # Test grabbing the max of the "Goals" column
        max_goals = grab_max(self.dataframe, "Goals")
        self.assertIsInstance(max_goals, float)

    def test_generate_summary_statistics(self):
        # Test generating summary statistics
        summary_stats = generate_summary_statistics(self.dataframe)
        self.assertIsNotNone(summary_stats)
        # Check that the summary contains statistics for numeric columns
        self.assertIn("Goals_mean", summary_stats.columns)
        self.assertIn("Goals_median", summary_stats.columns)
        self.assertIn("Goals_std", summary_stats.columns)

    def test_group_by(self):
        # Test grouping by a column (e.g., Nationality)
        nationality_counts = group_by(self.dataframe, "Nationality")
        self.assertIsNotNone(nationality_counts)
        self.assertIn("Nationality", self.dataframe.columns)

    def test_build_log_histogram(self):
        # Test that the histogram is generated and saved
        output_file = "test_histogram.png"
        build_log_histogram(self.dataframe, "Goals", output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)  # Clean up the test file

    def test_create_scatter(self):
        # Test that the scatterplot is generated and saved
        output_file = "test_scatter.png"
        create_scatter(self.dataframe, ["Goals", "Assists"], output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)  # Clean up the test file


if __name__ == "__main__":
    unittest.main()
