import pandas as pd


class File:
    file = None
    length = None
    def __init__(self, filename):
        self.file = pd.read_csv(filename)
        self.length = len(self.file)

    def getColumn(self, columnname, start = 0, stop=None, step=None):
        return self.file[columnname][start:stop:step]

    def getAllColumns(self):
        return self.file.columns

    def topRowsFrom(self, rows):
        return self.file.head(rows)

    def bottomRowsFrom(self, rows):
        return self.file.tail(rows)

    def getRowSlice(self, start, stop=None, step=None):
        return self.file.iloc[start:stop:step]

    def getSpecificElementInRow(self, row, element):
        return self.file.iloc[row, element]

    def SearchSpecificParam(self, column, param):
        return self.file.loc[self.file[column] == param]

    def getRaw(self):
        return self.file

    def getAscending(self, metric, ascendingBool):
        return self.file.sort_values(metric, ascending=ascendingBool)

    def set(self, col, pos, val):
        self.file.iloc[col, pos] = val

    def addCol(self, name, col):
        self.file[name] = col
        self.length += 1

    def setCol(self, name, col):
        self.file[name] = col

class Series(File):
    def __init__(self, series):
        self.file = series.copy()




