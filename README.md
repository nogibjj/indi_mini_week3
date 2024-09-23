[![Test](https://github.com/nogibjj/indi_mini_week3/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/nogibjj/indi_mini_week3/actions/workflows/test.yml)
[![Install](https://github.com/nogibjj/indi_mini_week3/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/indi_mini_week3/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/indi_mini_week3/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/indi_mini_week3/actions/workflows/format.yml)
[![Lint](https://github.com/nogibjj/indi_mini_week3/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/indi_mini_week3/actions/workflows/lint.yml)
![image](https://github.com/user-attachments/assets/e852ccc6-044b-4eed-9cc5-f94c5775b8af)


Jay Liu Individual Project #1


Youtube link

https://youtu.be/M2yzBmBC8VI


Purpose of the Project


The purpose of this project is to analyze a dataset related to soccer players, generating summary statistics and visualizations to provide insights into player performance, such as goals, assists, and positions. The project primarily uses Pandas for data manipulation and Matplotlib for visualizations. The continuous integration pipeline is set up using GitHub Actions for automated testing, linting, and formatting.

Source of Data:


The dataset is sourced locally as player_overview.csv. This dataset contains information about soccer players, including details such as nationality, position, goals, and assists.


Visiualization:


goal_log


<img width="591" alt="Screenshot 2024-09-23 at 6 57 06 PM" src="https://github.com/user-attachments/assets/f059c3ab-ebf9-4dcb-84f7-414cc9f6d783">


goal and assist


<img width="589" alt="Screenshot 2024-09-23 at 6 57 12 PM" src="https://github.com/user-attachments/assets/4781734c-6e6c-419a-b0a7-3d1a12a66caa">



Project Structure:


Directory:


Jay_Liu_IDS706_Week3_Individual/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.ipynb
├── main.py
├── Makefile
├── mylib/
│   ├── __init__.py
│   └── lib.py
├── README.md
├── requirements.txt
├── test_lib.py
└── test_main.py

Key Files:

main.py: The main script that loads the dataset, calls the library functions, and generates visualizations.

mylib/lib.py: The library file containing all the core functions for loading datasets, generating summary statistics, grouping data, and creating visualizations.

test_lib.py: Tests the functions within lib.py to ensure correctness.

test_main.py: Tests the functionality of the main.py script, verifying that it works as expected.

Makefile: Automates the tasks of installing dependencies, linting, formatting, and running tests.

requirements.txt: Lists the Python packages required for the project, including Pandas, Matplotlib, and testing libraries.

.github/workflows/: Contains CI workflows for linting, testing, formatting, and installation, enabling automated testing and code quality checks on GitHub.
Installation

To install the required packages, run the following command:

make install


make install

This will install the dependencies listed in requirements.txt.

Lint

To lint the code using Ruff, execute:

make lint


Test

To run the tests, execute:

make test

This will run tests for both the library functions and the main script using pytest.
 


