alphavit = " abcdefghijklmnopqrstuvwxyz "
n = 13
s = input().strip()
res = ''
for c in s:
    res += alphavit[(alphavit.index(c) + n) % len(alphavit)]
print('Result: "' + res + '"')