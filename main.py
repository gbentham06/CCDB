import pandas as pd


def findrow(df, item, column):
    try:
        return df.index[df[column] == item][0], True

    except IndexError:
        return None, False


def main():
    sweets = pd.read_csv("sweets.csv")
    while True:
        run(sweets)
        if input("would you like to keep going? ").lower() == 'n':
            break


def run(sweets):
    target = ''

    while not (findrow(sweets, target.lower(), 'sweet')[1]):
        target = input("pick a confectionary: ")

    row = findrow(sweets, target.lower(), 'sweet')[0]
    votes = sweets['votes'][row]

    total = []
    for column in sweets.columns:
        rating = -1
        if column == 'total' or column == 'votes' or column == 'sweet':
            continue
        while rating < 0 or rating > 10:
            rating = float(input(f'how would you rate {target}\'s {column} '))
        sweets.loc[row, column] = ((sweets.loc[row, column] * votes) + rating) / (votes + 1)
        total.append(sweets.loc[row, column])

    sweets.loc[row, 'total'] = round(sum([total[0] * 5, total[1] * 4, total[2] * 3,
                                          total[3] * 2, total[4] * 2, total[5]]) / 17, 2)
    sweets.loc[row, 'votes'] += 1

    sweets.to_csv('sweets.csv', index=False)


if __name__ == '__main__':
    main()
