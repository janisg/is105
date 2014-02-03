/*
 * Lab utvikling i IS-105 Jan2014
*/

#include <stdio.h>

void inplace_swap ( int *x, int *y ) {
	*y = *x ^ *y; /* Step 1 */
	*x = *x ^ *y; /* Step 2 */
	*y = *x ^ *y; /* Step 3 */
}

void reverse_array ( int a[], int cnt ) {
	int first, last;
	
	for ( first = 0, last = cnt - 1; first < last; first++, last-- ) {
		// if (first != last) { - ikke den enkleste løsningen!
		// Man kan endre first <= last til first < last
			inplace_swap(&a[first], &a[last]);
			printf("a[%d] = %d, a[%d] = %d\n", first, a[first], last, a[last]);
		// }
	}

}

int main() {
	int a, b;
	int i;
	int *pa, *pb;
	int aa[] = {1, 2, 3, 4, 5};
	a = 105; pa = &a;
	b = 85; pb = &b;

	printf("a=%d b=%d\n", *pa, *pb);
	inplace_swap(pa, pb);
	printf("a=%d b=%d\n", *pa, *pb);

	reverse_array(aa, 5);
	for (i = 0; i < 5; i++) {
		printf("a[%d] = %d\n", i, aa[i]);
	} 

}
