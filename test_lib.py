import pytest
import os
import pandas as pd
from mylib import lib

DATASET_PATH = "player_overview.csv"


@pytest.fixture
def dataset():

    df = lib.load_dataset(DATASET_PATH)
    return df


def test_load_dataset():

    df = lib.load_dataset(DATASET_PATH)
    assert isinstance(
        df, pd.DataFrame
    ), "The dataset should be loaded as a Pandas DataFrame"
    assert not df.empty, "The dataset should not be empty"


def test_print_head(dataset):

    head = lib.print_head(dataset, n=5)
    assert len(head) == 5, "The function should return 5 rows by default"
    assert isinstance(head, pd.DataFrame), "The output should be a Pandas DataFrame"


def test_generate_summary_statistics(dataset):

    summary_stats = lib.generate_summary_statistics(dataset)
    assert isinstance(
        summary_stats, pd.DataFrame
    ), "The output should be a Pandas DataFrame"
    assert (
        "count" in summary_stats.index
    ), "The summary statistics should include a 'count' row"


def test_group_by(dataset):

    grouped = lib.group_by(dataset, "Position")
    assert isinstance(grouped, pd.Series), "The output should be a Pandas Series"
    assert not grouped.empty, "The grouped result should not be empty"


def test_build_log_histogram(dataset):

    output_file = "test_histogram.png"
    lib.build_log_histogram(dataset, "Goals", output_file)
    assert os.path.exists(output_file), "The histogram file should be saved"
    os.remove(output_file)


def test_create_scatter(dataset):

    output_file = "test_scatter.png"
    lib.create_scatter(dataset, "Appearances", "Goals", output_file)
    assert os.path.exists(output_file), "The scatter plot file should be saved"
    os.remove(output_file)


def test_save_to_markdown(dataset):

    summary_stats = lib.generate_summary_statistics(dataset)
    output_file = "test_summary.md"
    lib.save_to_markdown(summary_stats, output_file)
    assert os.path.exists(output_file), "The markdown file should be saved"
    os.remove(output_file)
