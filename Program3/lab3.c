/* Program to demonstrate how to over write the
* return address inside of function
* we will use a global variable to store
* the address we want to go to on return
* and we will use an array in the function to
* seek the location and replace with the new value

 

Shaun Cooper

2020 September



Jeffrey Lansford
Program 3
9/18/2020
Program to show how the runtime stack works and how language uses memory. 
*/
#include <stdio.h>

// dummy function which makes one important change

void f()
{

    unsigned int *A;
    int i;

    // varibles to use to increase activation record
    // we can leave all the varibles declared, as the optimizer will not allocate varibles not assigned
    int j;
    int k;
    int l;
    int m;
    int n;

    j = 12;
    k = 13;
    A = (unsigned int *)&A;

    for (i = 0; i <= 10; i++)
        printf("%d %u\n", i, A[i]);

    // add two to index for two varibles added
    A[8] = A[8] + 10;
    printf("A is %u \n", A);
    for (i = -4; i <= 10; i++)
        printf("%d %u\n", i, A[i]);
}

int main()
{

    int A[100];
    unsigned int L[400];
    L[0] = 100;
    L[1] = 200;
    L[2] = 300;
    L[3] = 400;

    printf("A[] is at %u \n", A);
    printf("L[] is at %u \n", L);

    for (int i = 0; i < 100; i++)
        A[i] = i;

    for (int i = 0; i <= 3; i++)
        printf("L:%d %u\n", i, L[i]);

    printf("main is at %lu \n", main);

    printf("f is at %lu \n", f);
    printf("I am about to call f\n");
    f();
    printf("I called f\n");

    // tests to see how the SP changes
    // L[0] = 100;
    printf("here \n");
    for (int i = 0; i <= 3; i++)
        printf("L:%d %u\n", i, L[i]);

out:
    printf(" I am here\n");
}
