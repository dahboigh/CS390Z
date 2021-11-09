# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: correlation analysis and linear regression (attempt)

import pandas as pd
import os
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# definitions/parameters
DATA_FOLDER = os.path.join('..', 'data')
DATASET_NAME = 'country_indicators.csv'
COLUMNS = ['country', 'gini', 'edu_index']


if __name__ == "__main__":
    # TODO: create a pandas data frame from the CSV file
    # (optional) TODO: define the country as the index for the data frame
    # (optional) TODO: remove all columns except 'gini' and 'edu_index' from the data frame
    df = pd.read_csv(
        os.path.join(DATA_FOLDER, DATASET_NAME),
        index_col=COLUMNS[0],
        usecols=COLUMNS
    )

    # TODO: remove any country (index) that does not have both 'gini' and 'edu_index' values
    df.dropna(inplace=True, how='any')

    # TODO: compute and display the correlation matrix between 'gini' and 'edu_index'
    print("Correlation between Global Inequality Index and Education Index")
    print(df.corr())

    # TODO: attempt a linear regression model, displaying the obtained r2 score
    x = df[COLUMNS[1]].values.reshape(-1, 1)
    y = df[COLUMNS[2]].values
    model = LinearRegression().fit(x, y)
    r2 = model.score(x, y)
    print("r2 score:", r2, "\n")

    # TODO: produce a visualization of the data points and the fitted line
    y_predict = model.predict(x)
    plt.scatter(x, y)
    plt.plot(x, y_predict, c="black")
    plt.show()
