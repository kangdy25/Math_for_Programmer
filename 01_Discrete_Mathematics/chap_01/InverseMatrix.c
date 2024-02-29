#include <stdio.h>
#include <process.h>

#define MAX 3
typedef float mxtype[MAX][MAX];
void matrixout(mxtype);

void main() {
    mxtype mxa, inversemx;
    int l, n;

    float sumx, sumy;
    float determins;

    printf("please input 3 by 3 matrix : \n");
    printf("ex) 1 2 3\n 4 5 6\n 7 8 9\n\n");

    // read matrix
    for(int i = 0; i < MAX; i++) {
        for(int j = 0; j < MAX; j++) {
        scanf("%f",&mxa[i][j]);
        }
    }
    
    // write images of matrix A
    printf("%5cmatrix A\n",' ');
    matrixout(mxa);

    // determinant
    sumx = 0;
    sumy = 0;
    determins = 0;

    for(int j = 0; j < MAX; j++) {
        l = (j + 1) % MAX;
        n = (j + 2) % MAX;
        sumx += mxa[0][j] * mxa[1][l] * mxa[2][n];
        sumy += mxa[0][j] * mxa[1][n] * mxa[2][l];
    }
    determins = sumx - sumy;
    putchar('\n');
    printf("%5cdeterminant%7c:%15E\n",' ',' ',determins);
    
    // inverse matrix
    if (determins == 0) {
        printf("%5cinverse matrix does not exist\n",' ');
        exit(1);
    }
    for(int i = 0; i < MAX; i++)
    for(int j = 0; j < MAX; j++) {
        if(i==j) {
            switch(i) {
                case 0 : 
                    inversemx[0][0] = mxa[1][1] * mxa[2][2] - mxa[1][2] * mxa[2][1]; 
                    break;
                case 1 : 
                    inversemx[1][1] = mxa[0][0] * mxa[2][2] - mxa[0][2] * mxa[2][0]; 
                    break;
                case 2 :
                    inversemx[2][2] = mxa[0][0] * mxa[1][1] - mxa[0][1] * mxa[1][0]; 
                    break;
            }
        } else {
            l = i + j;
            switch(l) {
                case 1 :
                    l = 2; 
                    break;
                case 2 :
                    l = 1; 
                    break;
                case 3 :
                    l = 0; 
                    break;
            }
            inversemx[i][j] = (mxa[i][l] * mxa[l][j] - mxa[i][j] * mxa[l][l]) * 1.0;
        }
    }
    for(int i = 0; i < MAX; i++) {
        for(int j = 0; j < MAX; j++) {
            inversemx[i][j] /= determins;
        }
    }
    printf("\n%5cinverse matrix\n",' ');
    matrixout(inversemx);
}

void matrixout(mxtype mx) {
    putchar('\n');

    for(int i = 0 ; i < MAX; i++) {
        for(int j = 0 ; j < MAX; j++) {
            printf("%15E ",mx[i][j]);
        }
        printf("\n");
    }
}