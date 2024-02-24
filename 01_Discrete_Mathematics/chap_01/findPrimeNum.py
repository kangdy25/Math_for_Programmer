from __future__ import print_function
import sys

def printf(str, *args):
    print(str % args, end='')

printf("입력(Input)에 대한 소수 판별을 해드립니다.\n소수 판별하기 위한 N값을 입력해 주세요 : ")
inputvalue = int(sys.stdin.readline())

for i in range(2, inputvalue):
    if inputvalue % i == 0 and inputvalue != i:
        printf("\ninput number -->%5d Not Prime number!!\n" % inputvalue)
        sys.exit(0);

if inputvalue > 1:
    printf("\ninput number -->%5d Prime number!!\n" % inputvalue)
else:
    printf("\ninput number -->%5d Not Prim1e number!!\n" % inputvalue)

sys.stdin.readline()