from __future__ import print_function
from sys import stdin

def printf(str, *args):
    print(str % args, end='')

maxvalue = 3

c = [[False for _ in range(maxvalue)] for _ in range(maxvalue)]
d = [[False for _ in range(maxvalue)] for _ in range(maxvalue)]
e = [[False for _ in range(maxvalue)] for _ in range(maxvalue)]

def mat_compute(a, b):
    for i in range(0, maxvalue):
        for j in range(0, maxvalue):
            for k in range(0, maxvalue):
                c[i][j] = a[i][j] and b[i][j]
                d[i][j] = a[i][j] or b[i][j]
                if k == 0:
                    e[i][j] = a[i][k] * b[k][j]
                else:
                    e[i][j] = e[i][j] or (a[i][k] and b[k][j])

def print_matrix(x):
    for i in range(0, maxvalue):
        printf("\n")
        for j in range(0, maxvalue):
            printf("%2d" % x[i][j])
    printf("\n")

a = [[False for _ in range(maxvalue)] for _ in range(maxvalue)]
b = [[False for _ in range(maxvalue)] for _ in range(maxvalue)]

printf("\n")
printf("부울 행렬 A(3*3)를 입력하세요.\n(0과 1만 사용하세요)\n")
printf("ex) 0 1 0\n 0 0 0\n 1 0 1\n\n")

list = []
while len(list) < maxvalue * maxvalue:
    list += stdin.readline().strip("\n").split()
for i in range(0, maxvalue):
    for j in range(0, maxvalue):
        a[i][j] = bool(int(list[i*maxvalue + j]))    
print(a)
printf("\n 부울 행렬 B(3*3)을 입력하세요.\n")

list = []
while len(list) < maxvalue * maxvalue:
    list += stdin.readline().strip("\n").split()
for i in range(0, maxvalue):
    for j in range(0, maxvalue):
        b[i][j] = bool(int(list[i*maxvalue + j]))
print(b)
mat_compute(a,b)
printf("\n")

printf("A MEET B\n")
print_matrix(c)
printf("\n")

printf("A JOIN B\n")
print_matrix(d)
printf("\n")

printf("A Boolean product B\n")
print_matrix(e)
stdin.readline()