#include <stdio.h>
#include <string.h>

int main(void)
{
	char input[1001];
	fgets(input,1001,stdin);
	int i;
	
	for (i=0;i<strlen(input);i++)
	{
		if (input[i]==' ')
		{
			input[i]='*';
		}
	}
	printf("�ٲ� ���ڿ��� %s�̴�",input);
	return 0;
}
