/*
 * Lab utvikling i IS-105 Jan2014
*/

#include <stdio.h>

/* Setter bits i x til 1 der hvor de er 1 i m */
int bis(int x, int m) {
	// x = 00001000 01010101
	// m = 00011111 11000011
	// z = 00011111 11010111
	return x;	
}
/* Setter bits i x til 0 der hvor de er 1 i m */
int bic(int x, int m) {
	return 0x00;
}

int bool_or(int x, int y) {
	int result = 
	return result;
}

int bool_xor(int x, int y) {
	int result = 
	return result;
}

int main() {

	

	return 0;
}
/*
 12345 39 30 00 00 (little endian)
-12345 c7 cf ff ff (little endian)
00 00 3   0    3   9 (big endian)
      00110000 00111001
ff ff 11001111 11000110 one's complement (big endian)
ff ff c   f    c   6    + 1 
ff ff c   f    c   7    two's complement (big endian)
ff ff cf c7
c7 cf ff ff (little endian)
*/
