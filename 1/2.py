import re

input = open('input.txt', 'r').read().strip().split('\n')
translation = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
translate = lambda x: translation.get(x, x)
ans = 0
for line in input:
    pattern = r'(?=(\d|' + '|'.join(translation.keys()) + '))'
    digits = re.findall(pattern, line)
    cv = int(translate(digits[0]) + translate(digits[-1]))
    ans += cv
print(ans)
