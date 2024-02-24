#include <stdio.h>
#include <windows.h>

void main() {
    int i, input;
    printf("입력(Input)에 대한 소수 판별을 해드립니다.\n");
    printf("소수 판별하기 위한 N값을 입력해 주세요 : "); 
    scanf("%d", &input);
    
    for(i = 2; i < input; i++) {
        if(input % i == 0 && input != i) {
            printf("\ninput number -->%5d Not Prime number!!\n", input);
            system("PAUSE");

            return;
        }
    }

    if (input > 1) {
        printf("\ninput number -->%5d Prime number!!\n", input); 
    } else {
        printf("\ninput number -->%5d Not Prime number!!\n", input);
    }

    system("PAUSE");
}