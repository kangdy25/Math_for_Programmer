from __future__ import print_function
from sys import stdin, exit

def printf(str, *args):
    print(str % args, end='')

MAX = 3

def matrixout(mx):
    print("\n")
    for i in range(0, MAX):
        for j in range(0, MAX):
            printf("%15E " % mx[i][j])
        printf("\n")

mxa = [[0 for _ in range(MAX)] for _ in range(MAX)]
inversemx = [[0 for _ in range(MAX)] for _ in range(MAX)]

printf("please input 3 by 3 matrix : \n");
printf("ex) 1 2 3\n 4 5 6\n 7 8 9\n\n");

# read matrix
list = []
while len(list) < MAX * MAX:
    list += stdin.readline().strip("\n").split()
for i in range(0, MAX):
    for j in range(0, MAX):
        mxa[i][j] = float(list[i*MAX + j])

# write images of matrix A
printf("%5cmatrix A\n" % ' ')
matrixout(mxa)

# determinant
sumx = 0
sumy = 0
determins = 0

for j in range(0, MAX):
    l = (j+1) % MAX
    n = (j+2) % MAX
    sumx += mxa[0][j]*mxa[1][l]*mxa[2][n]
    sumy += mxa[0][j]*mxa[1][n]*mxa[2][l]

determins = sumx - sumy
printf("\n")
printf("%5cdeterminant%7c:%15E\n" %(' ',' ',determins) )

# inverse matrix
if determins == 0:
    printf("%5cinverse matrix does not exist\n" % ' ')
    exit(1)

for i in range(0, MAX):
    for j in range(0, MAX):
        if i == j:
            if i==0:
                inversemx[0][0] = mxa[1][1]*mxa[2][2]-mxa[1][2]*mxa[2][1]
            elif i==1:
                inversemx[1][1] = mxa[0][0]*mxa[2][2]-mxa[0][2]*mxa[2][0]
            elif i==2:
                inversemx[2][2] = mxa[0][0]*mxa[1][1]-mxa[0][1]*mxa[1][0]
            else:
                l = i+j
                l = {1:2, 2:1, 3:0}.get(l)
                inversemx[i][j]=(mxa[i][l]*mxa[l][j]-mxa[i][j]*mxa[l][l])*1.0

for i in range(0, MAX):
    for j in range(0, MAX):
        inversemx[i][j] /= determins
printf("\n%5cinverse matrix\n" % ' ')
matrixout(inversemx)