example = {'Time': [7, 15, 30],
           'Distance': [9, 40, 200],}

input = {'Time': [41, 66, 72, 66],
           'Distance': [244, 1047, 1228, 1040],}

table = input
ans = 1

for i in range(len(table['Time'])):
    time = table['Time'][i]
    distance = table['Distance'][i]
    for i in range(time):
        if i * (time - i) > distance:
            lo = i
            break
    for i in reversed(range(time)):
        if i * (time - i) > distance:
            hi = i
            break
    ans *= hi - lo + 1
    
print(ans)