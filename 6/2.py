example = {'Time': 71530, 'Distance': 940200}

input = {'Time': 41667266, 'Distance': 244104712281040}

table = input

time = table['Time']
distance = table['Distance']

for i in range(time):
    if i * (time - i) > distance:
        lo = i
        break
for i in reversed(range(time)):
    if i * (time - i) > distance:
        hi = i
        break
ans = hi - lo + 1
print(ans)