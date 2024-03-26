n = input()
s = n.replace('-', '')
n = [len(i) for i in n.split('-')]
if s.isdigit() and s[0] == '7' and len(s) == 11 and n == [1, 3, 3, 4]:
    print('YES')
elif s.isdigit() and len(s) == 10 and n == [3, 3, 4]:
    print('YES')
else:
    print('NO')
