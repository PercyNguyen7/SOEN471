# Group 27 - Assignment 2: SmartCart

## Setup Instructions

### Google Colab (Require Sign In)

1. Navigate to https://colab.research.google.com/
2. Sign in your Google Account
3. Upload the provided ipynb file
4. Click "Run all" and see each output underneath their respective cell

### Run notebook in VsCode

1. Verify you have Python installed with `python --version`. If not, please download from https://www.python.org/downloads/.
2. Write the command `pip list` in the terminal and verify that you have the following libraries installed: pandas, numpy, matplotlib, seaborn, scikit-learn, mlxtend, networkx
3. If not, please install via `pip install LIBRARY_NAME`
4. Open the ipynb file in VsCode
5. Select the Python kernel top right
6. Click on Run All and see each output underneath their respective cell

## Resizing Table Rows

Note that we limited some dataframe results to only show a fraction of the output as output tables may take up up hundreds of rows.
If you wish to see more or fewer options, please edit `iloc[r:c]` or `head(r)` where `r` represents the number of rows and `c` represenst the number of columns.
