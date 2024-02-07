#include <stdio.h>
#define x 4 

int main(void)
{
	int i,j;
	for(i=0;i<=x;i++)
	{
		for(j=x-i-1;j>0;j--)
		{
			printf("");
		}
		for(j=0;j<i;j++)
		{
			printf("%d ",i);
		}
		printf("\n");
	}
	return 0;
}
