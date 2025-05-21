#include <stdio.h>
#include <stdlib.h>

int nums[] = {0,1,2,2,3,0,4,2}; // Input array
int val = 2; // Value to remove

int removeElement(int* nums, int numsSize, int val) {
	int j=0;
    int ret[numsSize+1] = {};

    for (int i=0; i<numsSize; i++) {
		if(nums[i]!=val) {
			ret[j] = nums[i];
			j++;
		}
	}

	for (int i=0; i<j; i++) {
		nums[i] = ret[i];
	}

	int k = numsSize - j;
    printf("Removed elements: %d\n", k);

    for (int i=0; i< j; i++) {
	    printf("%d", nums[i]);
    }

    printf("\n");

	return j;
}

int main() {

	int originalSize=(int)sizeof(nums)/sizeof(nums[0]);

	printf("originalSize: %d\n", originalSize);

	int k = removeElement(nums, originalSize, val);
	printf("Removed elements: %d\n", k);

	return 0;
}
