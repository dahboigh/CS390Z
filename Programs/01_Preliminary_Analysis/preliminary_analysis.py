import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import pandas as pd
import matplotlib.pyplot as plt


# definitions/parameters
year = 2015
url = "https://ourworldindata.org/grapher/health-expenditure-and-financing-per-capita?tab=table"
title = f"Health Expenditure and Financing for {year}"
x_label = f"Amount spent per capita\n(in 2010 international dollars)"

# Retrieve page data as json
response = requests.session().get(url)
soup = BeautifulSoup(response.content, "html.parser")

## Data displayed on page is pulled from another location;
## Find the data location and retrieve its contents as json
data_relative_link = soup.find("link", {"as": "fetch"})['href']
data_url = urljoin(url, data_relative_link)
response = requests.session().get(data_url).content
raw_data = json.loads(BeautifulSoup(response, 'html.parser').string)

# Ready information from json for use in DataFrame
entities = raw_data['variables']['1871']['entities']
years = raw_data['variables']['1871']['years']
values = raw_data['variables']['1871']['values']

## Replace entity reference codes with country names
for i in range(len(entities)):
    key = str(entities[i])
    entities[i] = raw_data["entityKey"][key]["name"]

## Create DataFrame with only records for the specified year
df = pd.DataFrame({"Country": entities, "Year": years, "Value": values})
df = df.loc[df["Year"] == year, ["Country", "Value"]]
data = df['Value'].astype('float64')

# Calculate and Report Statistics
count, mean, std, min, q1, median, q3, max = data.describe()
iqr = q3 - q1
lower = int(q1 - iqr * 1.5)
upper = int(q3 + iqr * 1.5)

stats = "-- Summary Statistics --\n"
stats += f"Mean: ${int(mean)}\n"
stats += f"Median: ${int(median)}\n"
stats += f"Range: ${int(max-min)}\n"
stats += f"Std Dev: ${int(std)}\n"
print(stats)

outliers = {"Low": [lower, df.loc[df["Value"] < lower]], "High": [upper, df.loc[df["Value"] > upper]]}
for i in outliers:
    results = outliers[i][1]
    print(f"-- {i} Outliers --  (Threshold = ${outliers[i][0]})")
    print("(None)\n") if len(results) == 0 else print(results.to_string(header=False, index=False), '\n')

# Configure Histogram
fig, ax = plt.subplots()
bins = list(range(0, 10000, 1000))
counts, bins, patches = ax.hist(data, bins=bins, edgecolor='black')
ax.set_xticks(bins)
plt.title(title)
plt.xlabel(x_label)
plt.ylabel('y_label')

# Configure Box-and-Whisker
fig2, ax2 = plt.subplots()
ax2.boxplot(data, vert=False)
ax2.set_xlabel(x_label)
ax2.set(ylabel=None)
ax2.set(yticklabels=[])
ax2.tick_params(left=False)
ax2.set_title(title)

plt.show()