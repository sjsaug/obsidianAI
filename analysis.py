import pandas
import matplotlib.pyplot as plot

class Analysis:
    def __init__(self, type, file_path):
        if type == 'csv':
            self.data = pandas.read_csv(file_path)
        if type == 'parquet':
            self.data = pandas.read_parquet(file_path)

    def summary_statistics(self):
        return self.data.describe()

    def get_shape(self):
        return self.data.shape

    def show_rows(self, rows):
        return self.data.head(rows)
    
    def get_columns(self):
        return list(self.data.columns)
    
    def missing_values(self):
        return self.data.isnull().sum()
    
    def histogram(self, column):
        self.data[column].hist(bins=30)
        plot.title(f'Histogram of {column}')
        plot.xlabel(column)
        plot.ylabel('Frequency')
        plot.show()