from analysis import Analysis


def eda():
    ngsim = Analysis('data/ngsim.csv')
    n = 5

    print(f'Rows 1 through {n}\n{ngsim.show_rows(n)}')
    print(ngsim.get_shape())
    print(ngsim.summary_statistics())
    print(ngsim.get_types())
    print(ngsim.missing_values())

if __name__ == "__main__":
    eda()