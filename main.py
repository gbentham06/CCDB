import pandas as pd


def findrow(df, item, column):
    try:
        row_number = df.index[df[column] == item][0]
        return df.loc[row_number].values, True
    except IndexError:
        return None, False

def main():
    sweets = pd.read_csv("sweets.csv")
    while not(findrow(sweets, input().lower(), 'sweet')[1]):
        print('not found')

    print('found')