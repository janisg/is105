/*
 * Lab utvikling i IS-105 Jan2014
 * Sjekk ut hvor mye plass forskjellige datatyper i C tar
*/

#include <stdio.h>

typedef unsigned char *byte_pointer;

void show_bytes (byte_pointer start, int len) {

	int i;
	for (i = 0; i < len; i++) {
		printf(" %.2x", start[i]);
	}
	printf("\n");
}

void show_int(int x) {
	show_bytes((byte_pointer) &x, sizeof(int));
}

void show_float(float x) {
	show_bytes((byte_pointer) &x, sizeof(float));
}
void show_char(char x) {
	show_bytes((byte_pointer) &x, sizeof(char));
}
void show_double(double x) {
	show_bytes((byte_pointer) &x, sizeof(double));
}

int main() {
	int i;
	printf("int:-12345 "); 
	show_int(-12345);
	for (i = 1; i < 10; i++) {
		printf("int:%d     ", i); 
		show_int(i);
	}
	printf("float:12345.0 ");
	show_float(12345.0);
	printf("char:Z ");
	show_char('Z');
	printf("double:12345.0 ");
	show_double(12345.0);
	return 0;

}

