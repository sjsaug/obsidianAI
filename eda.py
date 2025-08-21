from analysis import Analysis
from dl import inference

def eda():
    #data = Analysis('csv', 'data/ngsim.csv')
    data = Analysis('parquet', 'data/data.parquet')
    n = 5

    print(f'\nROWS 1 THROUGH {n}\n{data.show_rows(n)}')
    print(f'\nSHAPE\n{data.get_shape()}')
    print(f'\nMISSING VALUES\n{data.missing_values()}')
    print(f'\nSUMMARY STATISTICS\n{data.summary_statistics()}')

    #data.histogram('Vehicle_ID')
    data.histogram('avgSpeed')

    inference('phi3:mini')

if __name__ == "__main__":
    eda()