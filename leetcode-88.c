#include <stdio.h>
#include <stdlib.h>

int comp (const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{ 
   for (int i=m; i< m+n; i++)
		{
			nums1[i] = nums2[i-m];
        }

    qsort(nums1, n+m, sizeof(int),comp);    
}


int main(int argc, char *argv[]) {

    int nums1[] = {0,0,3,0,0,0,0,0,0};
    int nums2[] = {-1,1,1,1,2,3};
    int m = 3;
    int n = 6;
    int nums1Size = sizeof(nums1)/sizeof(nums1[0]);
    int nums2Size = sizeof(nums2)/sizeof(nums2[0]);
 
    printf("nums1Size: %d\n", nums1Size);
    printf("nums2Size: %d\n", nums2Size);
    printf("m: %d\n", m);
    printf("n: %d\n", n);
    
    for (int i=0; i<nums1Size; i++){
		printf("%d,", nums1[i]);
	}
	printf("\n");

    for (int i=0; i<nums2Size; i++){
		printf("%d,", nums2[i]);
	}
	
    merge((int *)nums1, nums1Size, m, (int *)nums2, nums2Size,  n);

	printf("\nResult:");

    for (int i=0; i<m+n; i++) {
		printf("%d,", nums1[i]);
	}
	
	printf("\n");

    return 0;
}

