import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

pd.set_option('display.max_columns', None)
pd.set_option("display.width", None)

def main():
    df = pd.read_csv("./resources/customer_churn.csv")

    # Task 1
    display_data(df)
    df = handle_missing_values(df)
    exploratory_data_analysis(df)
    show_correlation(df)

    return

def display_data(df:DataFrame):
    print("\n\n----------Display Dataset structure----------")
    print(df.info())

    print("\n\n----------Summary statistics----------")
    print(df.describe())


def handle_missing_values(df:DataFrame):

    print("\n\n----------Handle missing values----------")
    if df.isnull().values.any():
        print("Removing all rows that have missing datas.")
        new_df = df.dropna()
        print(df.describe())
        return new_df
    else:
        print("There are no missing values, no handling is necessary.")
        return df

def exploratory_data_analysis(df:DataFrame):
    show_histogram(df)
    show_boxplot(df)


def show_histogram(df:DataFrame):
    filter_num_df(df).hist(bins=20, figsize=(12, 8))
    plt.tight_layout()
    plt.show()

def show_boxplot(df:DataFrame):
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=filter_num_df(df))
    plt.xticks(rotation=45)
    plt.show()

def show_correlation(df:DataFrame):
    corr_matrix = filter_num_df(df).corr()
    # print(corr_matrix)

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.show()


def filter_num_df(df:DataFrame):
    numeric_cols = df.select_dtypes(include="number").columns
    # print(df.select_dtypes(include="number").columns)

    # Return DataFrame without clientID column
    return  df[numeric_cols[1:]]


main()
