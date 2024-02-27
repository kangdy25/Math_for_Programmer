from __future__ import print_function
from sys import stdin

def printf(str, *args):
    print(str % args, end='')

arr_1 = [[1,2,3,4],[4,3,2,1],[2,5,7,9],[6,3,2,1]]
arr_2 = [[1,5,6,7],[8,3,1,7],[6,2,8,3],[9,2,1,2]]

# print Arr_1
printf("배열_1 : \n")
for i in range(0, 4):
    printf(" ")
for j in range(0, 4):
    printf("%4d" % arr_1[i][j])
printf("\n")
printf("\n\n")

# print Arr_2
printf("배열_2 : \n")
for i in range(0, 4):
    printf(" ")
for j in range(0, 4):
    printf("%4d" % arr_2[i][j])
printf("\n")
printf("\n\n")

# init res
res = [[0 for _ in range(4)] for _ in range(4)]

# multi Arr_1 Arr_2 with ( i , j , k )
printf("배열_1 * 배열_2 (i,j,k 순서로) : \n")
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            res[i][j] += arr_1[i][k] * arr_2[k][j]

# print res
for i in range(0, 4):
    printf(" ");
for j in range(0, 4):
    printf("%4d" % res[i][j])
printf("\n")

# ------------------------------------------------------------ # init res
res = [[0 for _ in range(4)] for _ in range(4)]

# multi Arr_1 Arr_2 with ( i , k , j )
printf("배열_1 * 배열_2 (i,k,j 순서로) : \n")
for i in range(0, 4):
    for k in range(0, 4):
        for j in range(0, 4):
            res[i][j] += arr_1[i][k] * arr_2[k][j]

# print res
for i in range(0, 4):
    printf(" ");
for j in range(0, 4):
    printf("%4d" % res[i][j])
printf("\n")
printf("\n\n결과는 같다. 그러나 실행시간은 차이가 난다.\n")

stdin.readline()