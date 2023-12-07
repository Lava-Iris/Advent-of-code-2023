import pandas as pd

df = pd.read_csv('input.txt', sep = ' ', header=None, names=['cards', 'bid'], )

def translate(card):
    if card == 'A':
        return 14
    elif card == 'K':
        return 13
    elif card == 'Q':
        return 12
    elif card == 'J':
        return 11
    elif card == 'T':
        return 10
    else:
        return int(card)

def find_type(cards):
    count = {}

    for card in cards:
        count[card] = count.get(card, 0) + 1
    
    vals = count.values()
    l = len(vals)

    if l == 1:
        return 1
    elif 4 in vals:
        return 2
    elif 3 in vals and l == 2:
        return 3
    elif 3 in vals:
        return 4
    elif 2 in vals and l == 3:
        return 5
    elif 2 in vals:
        return 6
    else:
        return 7

df['type'] = df['cards'].apply(find_type)

for i in range(5):
    df['card' + str(i)] = df['cards'].apply(lambda x, i=i: translate(x[i]))

df = df.sort_values(by=['type', 'card0', 'card1', 'card2', 'card3', 'card4'], ascending=[False, True, True, True, True, True])
df = df.reset_index(drop=True)
df['winning'] = df['bid'] * (df.index + 1)
ans = df['winning'].sum()
print(ans)


