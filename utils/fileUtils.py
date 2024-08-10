import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)  # D:\PythonWorkspace\Pytest-Framework
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')
print(TEST_DATA_DIR)


def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        return json.load(file)


# function to read data from csv file
def getCsvDataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)  # convert to list so that it is available outside the function
    return dictList

# print('~~~~~~~')
# result = getCsvDataAsDict('registerApiData.csv')
# print(result)


# get data from CSV as list
def getDataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        lines = list(reader)  # convert to list so that it is available outside the function
    return lines


# returns list of tuples, within tuples its "list of inputs" and a scalar value for output-status
def getDataAsTuple(filename):
    dataList = getDataAsList(filename)
    # newList = []
    # for lines in dataList:
    #     newList.append((lines[:2], lines[2]))
    # list comprehension
    # [expression(element) for element in oldList if condition]
    newList = [(lines[:2], lines[2]) for lines in dataList]
    return newList

print('~~~~~~~')
result = getDataAsList('registerApiDataWithStatus.csv')
print(result)
result = getDataAsTuple('registerApiDataWithStatus.csv')
print(result)


# we can create a dict with list of zipped keys and values
keys = ['a', 'b', 'c', 'd']
values = ['alpha', 'beta', 'delta']
d = dict(zip(keys, values))
print(d)
