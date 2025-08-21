from analysis import Analysis
from llm import inference

def eda():
    #data = Analysis('csv', 'data/ngsim.csv')
    data = Analysis('parquet', 'data/data.parquet')
    n = 5
    shape = data.get_shape()
    mvs = data.missing_values()
    stats = data.summary_statistics()

    print(f'\nROWS 1 THROUGH {n}\n{data.show_rows(n)}')
    print(f'\nSHAPE\n{shape}')
    print(f'\nMISSING VALUES\n{mvs}')
    print(f'\nSUMMARY STATISTICS\n{stats}')

    #data.histogram('Vehicle_ID')
    data.histogram('avgSpeed')

    inference('phi3:mini', shape, mvs, stats)

if __name__ == "__main__":
    eda()