# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Activity 11: similarity analysis of neighborhoods in the Denver metro area

from helper_methods import *

import os
import math
import pandas
import numpy as np
import matplotlib.pyplot as plt


# definitions/parameters
DATA_FOLDER = os.path.join('..', 'data')
CSV_FILE_NAME = 'denver_neighborhoods.csv'
columns = ['Neighborhood',  'Population', '2020 Average Sale Price', 'Schools Score', 'Crime Rank', 'X Factor Score']


def main():
    # Retrieve data from csv file
    file_exists(filepath := os.path.join(DATA_FOLDER, CSV_FILE_NAME), "Data file not found.")
    data = pandas.read_csv(filepath, index_col=0, usecols=columns)
    neighborhoods = data.index.values


    # Normalize dataset
    normalized = data.copy()
    for column in normalized.columns:
        min = normalized[column].min()
        max = normalized[column].max()
        normalized[column] = (normalized[column] - min) / (max - min)


    # Euclidean comparisons
    euclidean = []
    for neighborhood_1 in normalized.iterrows():
        row_data = []
        for neighborhood_2 in normalized.iterrows():
            a = normalized.loc[neighborhood_1[0]].values
            b = normalized.loc[neighborhood_2[0]].values
            row_data.append(eucl_dist(a, b))
        euclidean.append(row_data)


    # Configure Plot            extensive help from https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py
    fig, ax = plt.subplots()
    im = ax.imshow(euclidean)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(neighborhoods)))
    ax.set_yticks(np.arange(len(neighborhoods)))

    # ... and label them with the respective list entries
    ax.set_xticklabels(neighborhoods)
    ax.set_yticklabels(neighborhoods)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    plt.show()


def eucl_dist(a, b): 
    sum = 0
    for i in range(len(a)):
        sum += (a[i] - b[i])**2
    return int((1 - math.sqrt(sum / len(a))) * 100000) / 100000


if __name__ == "__main__":
    main()
