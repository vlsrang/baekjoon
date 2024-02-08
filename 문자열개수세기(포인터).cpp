#include <stdio.h>
#include <string.h>

int main(void)
{
	char input[1001];
	char *p=input;
	fgets(input,1001,stdin);
	int count=0;

	printf("문자열 길이는 %d이다",strlen(p));
	return 0;
}
