# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Homework 03 - HDI Visualization

from helper_methods import *

import os
import csv
import math
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import pandas

# definitions/parameters
DATA_FOLDER    = os.path.join('..', 'data')
HDI_FILE_NAME = 'hdi.csv'
TARGET_YEAR   = '2019'

bins = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
title = f"Human Development Index (HDI) in the World ({TARGET_YEAR})"
x_label = "HDI"
y_label = "Number of Countries"

def main():

    filepath = os.path.join(DATA_FOLDER, HDI_FILE_NAME)
    file_exists(filepath)
    data = pandas.read_csv(filepath)
    hdi_values = data.loc[data.Coverage == "Country"][TARGET_YEAR]

    plt.hist(hdi_values, bins=bins, align="left", rwidth=0.5)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

if __name__ == "__main__":
    main()
