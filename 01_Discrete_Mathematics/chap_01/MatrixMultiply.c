#include <stdio.h>
#include <windows.h>

int main() {
    int arr_1[4][4] = {{1,2,3,4},{4,3,2,1},{2,5,7,9},{6,3,2,1}};
    int arr_2[4][4] = {{1,5,6,7},{8,3,1,7},{6,2,8,3},{9,2,1,2}};
    int res[4][4] = {{0}};

    //p rint Arr_1
    printf("배열_1 : \n");
    for(int i = 0; i < 4; i++) {
        printf(" ");
        for(int j = 0; j < 4; j++) {
            printf("%4d",arr_1[i][j]);
        }
        printf("\n");
    }
    printf("\n\n");

    //print Arr_2
    printf("배열_2 : \n");
    for(int i = 0; i < 4; i++) {
        printf(" ");
        for(int j = 0; j < 4; j++) {
            printf("%4d",arr_2[i][j]);
        }
        printf("\n");
    }

    //init res
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            res[i][j] = 0;
        }
    }

    //multi Arr_1 Arr_2 with ( i , j , k )
    printf("배열_1 * 배열_2 (i,j,k 순서로) : \n");
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                res[i][j] += arr_1[i][k] * arr_2[k][j];
            }
        }
    }

    //print res
    for(int i = 0; i < 4; i++) {
        printf(" ");
        for(int j = 0; j < 4; j++) {
            printf("%4d",res[i][j]);
        }
        printf("\n");
    }

    //------------------------------------------------------------
    //init res
    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            res[i][j] = 0;
        }
    }
    //multi Arr_1 Arr_2 with ( i , k , j )
    printf("배열_1 * 배열_2 (i,k,j순서로) : \n");
    for(int i = 0; i < 4; i++) {
        for(int k = 0; k < 4; k++) {
            for(int j = 0; j < 4; j++) {
                res[i][j] += arr_1[i][k] * arr_2[k][j];
            }
        }
    }

    //print res
    for(int i = 0; i < 4; i++) {
        printf(" ");
        for(int j = 0; j < 4; j++) {
            printf("%4d",res[i][j]);
        }
        printf("\n");
    }
    printf("\n\n결과는 같다. 그러나 실행시간은 차이가난다.\n");

    system("PAUSE");
    return 0;
}