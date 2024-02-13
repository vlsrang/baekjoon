#include <stdio.h>

int main(void)
{
	int i,j;
	int in=0;
	int matrix[3][3]={0,};
	for (i=0;i<3;i++)
	{
		for (j=0;j<3;j++)
		{
			in++;
			matrix[i][j]=in;
			printf("%d ",matrix[i][j]);
		}
		printf("\n");
	}
	return 0;
 } 
