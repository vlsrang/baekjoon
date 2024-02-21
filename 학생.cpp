#include <stdio.h>
#include <stdlib.h>

struct student{
	int number;
	char name[10];
	char depart;

};
int main(void)
{
	int N;
	int i;
	struct student list[10];
	printf("N: ");
	scanf("%d", &N);

	for (i=0;i<N;i++)
	{
		scanf("%d %s %s",&list[i].number,list[i].name, &list[i].depart);
		printf("학번은 %d, 이름은 %s, 학과는  %s이다",list[i].number,list[i].name, list[i].depart);
	}

}
