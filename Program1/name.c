/*
    Jeffrey Lansford
    Program 1
    9/1/2020
    Input: no input
    Output: 
        JEFFREY LANSFORD
        HELLO
        WORLD
        memory locations main,foo,A,B,C,D, and S
    Preconditions: None
    Postconditions: None
*/
#include <stdio.h>
#include <stdlib.h>

// function todo 256^x
int square_256(int i) {
    int square = 1;
    int x;
    for (x = 0; x < i; x++) {
        square = square * 256;
    }
    return square;
}

// global variable for memory location test
int B = 20;

// function for memory test
int foo() {
    int E[20];
}

int main() {
    // Integer Array to store bytes of integers
    static int A[100];
    // Pointer to print integer array as string
    char *S;
    // Fill array with my name and hello for testing 0 byte
    A[0] = 'J' + ('E' * square_256(1)) + ('F' * square_256(2)) + ('F' * square_256(3));
    A[1] = 'R' + ('E' * square_256(1)) + ('Y' * square_256(2)) + (' ' * square_256(3));
    A[2] = 'L' + ('A' * square_256(1)) + ('N' * square_256(2)) + ('S' * square_256(3));
    A[3] = 'F' + ('O' * square_256(1)) + ('R' * square_256(2)) + ('D' * square_256(3));
    A[4] = '\n' + ('H' * square_256(1)) + ('E' * square_256(2)) + ('L' * square_256(3));
    A[5] = 'L' + ('O' * square_256(1)) + ('\n' * square_256(2)) + ('W' * square_256(3));

    // Line for testing 0 byte
    // A[5] = 'L' + (0 * square_256(1)) + ('O' * square_256(2)) + ('\n' * square_256(3));

    // fill rest of array to unsure test has worked
    A[6] = 'O' + ('R' * square_256(1)) + ('L' * square_256(2)) + ('D' * square_256(3));

    // fills element to make sure that it does not print anything else
    A[7] = 0;

    // sets char pointer to integer array
    S = A;
    // prints as char array
    printf("%s\n", S);
    // test for memory location of variables
    char *C = malloc(100);
    static int D[10];
    printf("Location of       main is %20u\n", main);
    printf("Location of        foo is %20u\n", foo);
    printf("Location of          B is %20u\n", &B);
    printf("Location of          D is %20u\n", D);
    printf("Location of         *C is %20u\n", C);
    printf("Location of          S is %20u\n", &S);
    printf("Location of          A is %20u\n", A);
    foo();
}
