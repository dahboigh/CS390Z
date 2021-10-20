# CS390Z - Introduction to Data Mining - Fall 2021
# Instructor: Thyago Mota
# Description: Homework 04 - show outliers

import csv
import os
import matplotlib.pyplot as plt
import re


# definitions/parameters
DATA_FOLDER = os.path.join('..', 'data')
CSV_FILE_NAME = 'denver_neighborhoods.csv'


def main():
    neighborhoods, matrix = create_matrix()
    bp = boxplot(matrix)

    dictionary = dict(zip(neighborhoods, matrix))

    verb_phrases = [
        "has a population much",
        "has homes priced much",
        "has a school score average much",
        "has a crime rate that is much",
        "has an X-Factor that is much"
    ]

    for i in range(len(bp['fliers'])):
        outliers = bp['fliers'][i].get_xydata()
        track_y = []                # prevent errors for identical y-values
        for x, y in outliers:
            phrase = verb_phrases[i]
            direction = 'higher' if y > 0.5 else 'lower'
            names = [key for key, value in dictionary.items() if value[i] == y]

            for name in names:
                if y not in track_y:
                    print(name, phrase, direction, "compared to others.")
            track_y.append(y)


# The code below was provided for the assignment, rearranged as independent methods
def create_matrix():
    matrix = []
    neighborhoods = []
    with open(os.path.join(DATA_FOLDER, CSV_FILE_NAME), 'rt') as csv_file:
        reader = csv.reader(csv_file)
        row_count = 0
        for row in reader:
            row_count += 1
            if row_count == 1:
                continue
            row[0] = re.sub('Washington', 'Was.', row[0])
            row[0] = re.sub('South', 'S.', row[0])
            neighborhoods.append(row[0])
            data = [int(row[1]), int(row[2]), float(row[3]), int(row[4]), float(row[5])]
            if row_count == 2:
                mins = list(data)
                maxs = list(data)
            else:
                for i in range(len(data)):
                    mins[i] = min(mins[i], data[i])
                    maxs[i] = max(maxs[i], data[i])
            matrix.append(data)
    return neighborhoods, [min_max(data, mins, maxs) for data in matrix]


def min_max(data, mins, maxs, interval=(0, 1)):
    return [
        int(((data[i] - mins[i]) / (maxs[i] - mins[i]) * (interval[1] - interval[0]) + interval[0]) * 100000) / 100000
        for i in range(len(data))]


def boxplot(matrix):
    columns = [[], [], [], [], []]
    for data in matrix:
        for i in range(5):
            columns[i].append(data[i])
    bp = plt.boxplot(columns)
    axes = plt.gca()
    axes.set_xticklabels(['pop', 'home$', 'schools', 'crime', 'x factor'])
    plt.title('Neighborhoods in the Denver Metro Area')
    plt.ylabel('Normalized Values')
    return bp


if __name__ == "__main__":
    main()
