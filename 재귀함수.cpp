#include <stdio.h>

void re(int count)
{	
	if (count<1)
	{
		return ;
	}
	else
		printf("%d\n",count); 
		re(count-1);
}
int main(void)
{
	re(50);
	
	return 0;
}
