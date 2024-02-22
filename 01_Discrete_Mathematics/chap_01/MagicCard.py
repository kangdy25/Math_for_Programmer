from __future__ import print_function
from sys import stdin

def printf(str, *args):
    print(str % args, end='')

def my_opening():
    printf("# 지금부터 여러분을 신비한 마술의 세계로 초대합니다.\n\n\n")
    printf("1 - 31의 숫자중 마음에 드는 숫자를 생각해 보세요. \n\n\n")

def my_card(index):
    cardname = chr(ord('A') + index - 1)
    while True:
        printf(" --------- %s 카드 ---------\n" % cardname )
        for i in range(0, 4):
            for j in range(0, 4):
                printf("%7d" % card[index-1][4*i + j])
            printf("\n")
        printf(" --------------------------\n")
        printf("\n\n")
        printf("%s 카드에 생각한 숫자가 있다면 YES(1번),\n" % cardname)
        printf("없다면 NO(0번)을 선택하여 주시기 바랍니다. : ")
        result = int(stdin.readline())
        printf("\n\n")
        if result>-1 and result<2:
            return result
        
def my_res(a,b,c,d,e):
    res = (e*2*2*2*2) + (d*2*2*2) + (c*2*2) + (b*2) + (a)
    printf("당신이 마음에 드는 숫자는 %d입니다.\n\n\n" % res);
    printf("어때요? 신기하죠!!\n");
    printf("지금까지 마술의 세계였습니다.\n\n");

card = [
    [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],
    [2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31],
    [4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31],
    [8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31],
    [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
]

my_opening()

printf("생각하셨어요? 시작하려면 엔터를 누르시오.")
stdin.readline()

print("\n\n")
a = my_card(1)
b = my_card(2)
c = my_card(3)
d = my_card(4)
e = my_card(5)

my_res(a,b,c,d,e)

stdin.readline()