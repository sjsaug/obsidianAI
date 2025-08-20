import pandas

class Analysis:
    def __init__(self, file_path):
        self.data = pandas.read_csv(file_path)

    def summary_statistics(self):
        return self.data.describe()

    def get_shape(self):
        return self.data.shape

    def show_rows(self, rows):
        return self.data.head(rows)
    
    def get_columns(self):
        return list(self.data.columns)
    
    def get_types(self):
        return self.data.dtypes
    
    def missing_values(self):
        return self.data.isnull().sum()