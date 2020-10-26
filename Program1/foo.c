#include <stdio.h>
int D;

int f() {
    int C[50];
    printf("Location of    C is %20u\n", C);
    return 0;
}
int main() {
    int A[100];
    static int B;

    printf("Location of main is %20u\n", main);
    printf("Location of    f is %20u\n", f);
    printf("Location of    B is %20u\n", &B);
    printf("Location of    D is %20u\n", &D);
    printf("Location of    A is %20u\n", A);
    f();
}
