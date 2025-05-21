+#include <stdio.h>
#include <stdlib.h>

int removeDuplicates(int* nums, int numsSize) 
{
	int j=0;
	
	for (int i=1; i < numsSize; i++)
		{
			if(nums[j] != nums[i])
			{
				j++;
				nums[j] = nums[i];
			}
		}
	
	return j+1;
}

int main()
{
	int nums[]={0,0,1,1,1,2,2,3,3,4};
	int numsSize=sizeof(nums)/sizeof(nums[0]);
	int i,j;
	
	for (i=0; i < numsSize; i++)
	{
		printf("%d,", nums[i]);
	}
	printf("\nnumsSize: %d\n", numsSize);
	
	j = removeDuplicates(nums, numsSize);
	
	for (i=0; i < j; i++)
	{
		printf("%d,", nums[i]);
	}
	printf("\nNew numsSize: %d\n", j);

	return 0;
}
