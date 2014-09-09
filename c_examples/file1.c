#include <stdio.h>
#include <stdlib.h>

#define MAX_LENGTH 100 

char** splitString(char line[], int* count) {
	char** wordArray = malloc(MAX_LENGTH / 2 * sizeof(char*));

	*count = 0;
	int i;
	int start=-1;
	for (i=0; i<MAX_LENGTH; i++) {
		if (line[i] == ' ' || line[i] == '\n') {
			if (start != -1) {
				line[i] = '\0';

				wordArray[*count] = line + start;
				start = -1;
				(*count)++;
			}
		} else {
			if (start == -1)
				start = i;
		}
	}

	if (start != -1) {
		wordArray[*count] = line + start;
		(*count)++;
	}

	return wordArray;
}

int main() {
	// Create the string buffer
	char line[MAX_LENGTH+1] = "This is a string of text";

	// Read in the string
	// fgets(line, MAX_LENGTH+1, stdin);

	int wordCount;
	char **theWords = splitString(line, &wordCount);

	int i;
	for (i=0; i<wordCount; i++)
		printf("%d. %s\n", i, theWords[i]);

	return 0;
}
