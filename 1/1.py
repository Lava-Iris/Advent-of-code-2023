import re

input = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for line in input:
    digits = re.findall(r'\d', line)
    cv = int(digits[0] + digits[-1])
    ans += cv
print(ans)