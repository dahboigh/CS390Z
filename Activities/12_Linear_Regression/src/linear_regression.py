# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: correlation analysis and linear regression (attempt)
import math
import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# definitions/parameters
DATA_FOLDER = os.path.join("..", "data")
DATASET_NAME = 'country_indicators.csv'
COLUMNS = ["country", "gdp_per_capita", "life_expectancy"]


def main():
    # TODO: create a pandas data frame from the CSV file
    # (optional) TODO: define the country as the index for the data frame
    # (optional) TODO: remove all columns except 'gdp_per_capita' and 'life_expectancy' from the data frame
    df = pd.read_csv(
        os.path.join(DATA_FOLDER, DATASET_NAME),
        index_col=COLUMNS[0],
        usecols=COLUMNS
    )

    # TODO: remove any country (index) that does not have both 'gdp_per_capita' and 'life_expectancy' values
    df.dropna(inplace=True, how='any')

    # TODO: compute and display the correlation matrix between 'gdp_per_capita' and 'life_expectancy'
    print("Correlation between GDP per Capita and Life Expectancy")
    print(df.corr(), "\n")

    # TODO: attempt a linear regression model, displaying the obtained r2 score
    x = df["gdp_per_capita"].values.reshape(-1, 1)
    y = df["life_expectancy"].values

    model = LinearRegression().fit(x, y)
    r_sq = model.score(x, y)
    print("r2 score:", r_sq, "\n")

    # TODO: produce a visualization of the data points and the fitted line
    y_pred = model.predict(x)
    plt.scatter(x, y)
    plt.plot(x, y_pred, c="black")
    plt.show()


if __name__ == "__main__":
    main()
