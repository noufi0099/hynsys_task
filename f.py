import re
n,m = input().split()
n,m = int(n), int(m)
matrix= []
for i in range(n):
    line=input()
    matrix.append(line)
transpose=list(zip(*matrix))
a = ''
for i in transpose:
        a=a + ''.join(i)
print(re.sub(r'(?<=[a-zA-Z0-9])[!@#$%&\s]+(?=[a-zA-Z0-9])', ' ', a))