import os
import pandas as pd


###############################################################################################################
# Pandas Data Structures    https://www.tutorialspoint.com/python_pandas/python_pandas_quick_guide.htm
#   Series          1D labeled homogeneous array, size-immutable
#   DataFrame       2D labeled, size-mutable tabular structure with potentially heterogeneously typed columns
#   Panel           General 3D labeled, size-mutable array
###############################################################################################################
# Series
#   pandas.Series( data, index, dtype, copy)
#           index must be same length as data. If not specified, it defaults to 0..n
#           dtype is inferred by default (strings as objects,
#               or can be specified: object, int64, float64, bool, datetime64, timedelta[ns], category
#
#       .axes       returns the row axis labels as a List
#       .dtype      returns the data type as numpy.dtype[object_]
#       .empty      returns Boolean: True if series is empty, False otherwise
#       .ndim       returns number of dimensions of underlying data as Integer. (A series is always 1)
#       .size       returns number of elements as Integer
#       .values     returns values as numpy.ndarray
#       .head(n)    returns first n rows as a Series.  If n is blank, returns 5
#       .tail(n)    returns last n rows as a Series.  If n is blank, returns 5
#
#   s = pd.Series(["male", "male", "female", "female", "male", "female", "male"])
#       s.axes:     [RangeIndex(start=0, stop=7, step=1)]
#       s.dtype:    object
#       s.empty:    False
#       s.ndim:     1
#       s.size:     7
#       s.values:   ['male' 'male' 'female' 'female' 'male' 'female' 'male']
###############################################################################################################
# DataFrame
#   pandas.DataFrame( data, index, dtype)
#         data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
#         df = pd.DataFrame(data, columns=['Name', 'Age'])
#
#         data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'], 'Age': [28, 34, 29, 42]}
#         df = pd.DataFrame(data)
#                      Name  Age
#                  0    Tom   28
#                  1   Jack   34
#                  2  Steve   29
#                  3  Ricky   42
#
#       .T          transposes rows and columns
#                            0     1      2      3
#                    Name  Tom  Jack  Steve  Ricky
#                    Age    28    34     29     42
#
#       .axes       returns the row axis labels as a List
#                   [RangeIndex(start=0, stop=4, step=1), Index(['Name', 'Age'], dtype='object')]
#
#       .dtypes     returns the data type as numpy.dtype[object_]
#                   Name    object
#                   Age      int64
#                   dtype: object
#
#       .empty      returns Boolean: True if series is empty, False otherwise
#                   False
#
#       .ndim       returns number of dimensions of underlying data as Integer. (A series is always 1)
#                   2
#
#       .size       returns number of elements as Integer
#                   8
#
#       .values     returns values as numpy.ndarray
#                   [['Tom' 28], ['Jack' 34], ['Steve' 29], ['Ricky' 42]]
#
#       .head(n)    returns first n rows as a DataFrame.  If n is blank, returns 5
#       .tail(n)    returns last n rows as a DataFrame.  If n is blank, returns 5
###############################################################################################################


data_folder = "data_files"
income = pd.read_csv(os.path.join(data_folder, "income.csv"))
series = pd.read_csv(os.path.join(data_folder, "iris.csv"))


column_names = income.columns
# an index object with the names of all columns
#     Index(['Index', 'State', 'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007',
#            'Y2008', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014', 'Y2015'],
#           dtype='object')


select_column_names = income.columns[0:4]
# an Index object with the names of columns 1-4
#     Index(['Index', 'State', 'Y2002', 'Y2003'], dtype='object')


column_data_types = income.dtypes
# a Series object with the data types of each column
#   Index    object
#   State    object
#   Y2002     int64
#   Y2003     int64
#   Y2004     int64
#   Y2005     int64
#   Y2006     int64
#   Y2007     int64
#   Y2008     int64
#   Y2009     int64
#   Y2010     int64
#   Y2011     int64
#   Y2012     int64
#   Y2013     int64
#   Y2014     int64
#   Y2015     int64


single_column_data_type = income['State'].dtypes
# a numpy.dtype[object_] with the data type of one column
#   object


row_column_count = income.shape
# a tuple with the row count and column count
# (51, 16)

first_5_rows = income.head()
# a DataFrame object with the data from only the first 5 rows
#       Index       State    Y2002    Y2003  ...    Y2012    Y2013    Y2014    Y2015
#     0     A     Alabama  1296530  1317711  ...  1186741  1852841  1558906  1916661
#     1     A      Alaska  1170302  1960378  ...  1512804  1985302  1580394  1979143
#     2     A     Arizona  1742027  1968140  ...  1907284  1363279  1525866  1647724
#     3     A    Arkansas  1485531  1994927  ...  1216675  1591896  1360959  1329341
#     4     C  California  1685349  1675807  ...  1921845  1156536  1388461  1644607
#
#    [5 rows x 16 columns]


first_n_rows = income.head(2)
# a DataFrame object with data from the first n rows  (here n=2)
#       Index    State    Y2002    Y2003  ...    Y2012    Y2013    Y2014    Y2015
#     0     A  Alabama  1296530  1317711  ...  1186741  1852841  1558906  1916661
#     1     A   Alaska  1170302  1960378  ...  1512804  1985302  1580394  1979143
#
#     [2 rows x 16 columns]


last_5_rows = income.tail()
# a DataFrame object with the last 5 rows
#        Index          State    Y2002    Y2003  ...    Y2012    Y2013    Y2014    Y2015
#     46     V       Virginia  1134317  1163996  ...  1262342  1647032  1706707  1850394
#     47     W     Washington  1977749  1687136  ...  1775787  1273834  1387428  1377341
#     48     W  West Virginia  1677347  1380662  ...  1462137  1683127  1204344  1198791
#     49     W      Wisconsin  1788920  1518578  ...  1729177  1510119  1701650  1846238
#     50     W        Wyoming  1775190  1498098  ...  1673668  1994022  1204029  1853858
#
#     [5 rows x 16 columns]


last_n_rows = income.tail(2)
# a DataFrame object with data from the first n rows  (here n=2)
#        Index      State    Y2002    Y2003  ...    Y2012    Y2013    Y2014    Y2015
#     49     W  Wisconsin  1788920  1518578  ...  1729177  1510119  1701650  1846238
#     50     W    Wyoming  1775190  1498098  ...  1673668  1994022  1204029  1853858
#
#     [2 rows x 16 columns]


unique_values = income.Index.unique()
# pandas.DataFrame.Column_Name.unique()
# returns all unique values as numpy.ndarray
# ['A' 'C' 'D' 'F' 'G' 'H' 'I' 'K' 'L' 'M' 'N' 'O' 'P' 'R' 'S' 'T' 'U' 'V' 'W']


unique_values_count = income.State.nunique()
# returns the number of unique values as an Integer
# 51


frequency = income.Index.value_counts()
# pandas.DataFrame.Column_Name.value_counts(ascending=False)   (if ascending=True, max frequency will be last)
#     M    8
#     N    8
#     I    4
#     A    4
#     W    4
#     C    3
#     O    3
#     K    2
#     D    2
#     S    2
#     T    2
#     V    2
#     G    1
#     H    1
#     F    1
#     L    1
#     P    1
#     R    1
#     U    1
#     Name: Index, dtype: int64


# pandas.DataFrame.drop(Column_Name(s), axis=0, inplace=False)
#   https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
#       axis:     delete by row if 0 (default); by column if 1
#       inplace:  do not change original data if False (default)

income = income[income.Index != "A"]

print(income.head())