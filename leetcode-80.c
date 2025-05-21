#include <stdio.h>
#include <stdlib.h>

int removeDuplicates(int* nums, int numsSize) 
{
	int j=0;
	int i=2;
	
 	while (i < numsSize-1)
		{
			if(nums[j] != nums[i])
			{
				j+=2;
   				nums[j] = nums[i];
   				nums[j+1] = nums[i];
				i++;
			}
			else
                {
				    i++;
				    j++;
                }
        }
	
	return j+1;
}

int main()
{
	int nums[]={1,1,1,2,2,3};
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
