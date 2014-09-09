#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 100


int main() {
	char line[MAX_LENGTH+1] = "This is a string of text";

	int counter;
	char **words = doSplit(line, &counter);

	int i;
	for (i=0; i<counter; i++)
		printf("%d. %s\n", i, words[i]);

	return 0;
}

char** doSplit(char line[], int* count) {
	char** myWordArray = malloc(MAX_LENGTH / 2 * sizeof(char*));

	*count = 0;
	int i;
	int j=-1;
	for (i=0; i<MAX_LENGTH; i++) {
		if (line[i] == ' ' || line[i] == '\n') {
			if (j != -1) {
				line[i] = '\0';

				myWordArray[*count] = line + j;
				j = -1;
				(*count)++;
			}
		} else {
			if (j == -1)
				j = i;
		}
	}

	if (j != -1) {
		myWordArray[*count] = line + j;
		(*count)++;
	}

	return myWordArray;
}
