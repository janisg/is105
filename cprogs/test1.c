/*
 * C program for sammenligning i IS-105 LAB3 Jan2014
*/

#include <stdio.h>

int main() {
    
	// Definisjon
    int i,j;
	int a[2];
	char c[2];
	int x,y;

	// Initialisering
	a[0] = 1;
	a[1] = 2;
	c[0] = 'a';
	c[1] = 'b';
	x = 105; // 01101001 = 64+32+8+1 = 105 
	y = 85;  // 01010101 = 64+16+4+1 = 85
	
  	for (i = 0; i < 2; i++) {
		for (j = 0; j < 2; j++) {
			printf("%d %c\n", a[i], c[j]);
		}
	}
    printf("\n\n");
	printf("sizeof(int) = %d\n", sizeof(int));
	printf("sizeof(char) = %d\n", sizeof(char));
	printf("XOR: %d %.8x\n", x^y, x^y); // 00111100 = 32+16+8+4 = 60 = 3c
	printf(" OR: %d %.8x\n", x|y, x|y);
    printf("AND: %d %.8x\n", x&y, x&y);
	printf("NOT: %d %x\n", ~x, ~x);	 // 10010110 = 

	for (i = 100; i < 110; i++) {
		printf("%d %x\n", ~i+1, ~i+1);
	}

	return 0;

}
    
