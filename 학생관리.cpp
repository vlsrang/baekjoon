#include <stdio.h>
#include <stdlib.h>

typedef struct _student{
	int number;
	double height;
	double weight;

} student;
int main(void)
{
	int N;
	int i;
	double havg=0.0;
	double wavg=0.0;
	student list[10]={'\0',0,0.0};
	printf("N: ");
	scanf("%d", &N);

	for (i=0;i<N;i++)
	{
		scanf("%d %lf %lf",&list[i].number,&list[i].height, &list[i].weight);
		havg += list[i].height;
		wavg == list[i].weight;
	}
	havg/=N;
	wavg/=N;
	printf("%.1lf %.1lf\n",havg, wavg);

	for (i=0;i<N;i++)
	{
		if (list[i].height<havg){
			if (list[i].weight<wavg)
				printf("%d below\n",list[i].number);
			else
				printf("%d average\n",list[i].number);
			}
		else{
			if (list[i].weight>wavg)
				printf("%d super\n",list[i].number);
			else
				printf("%d average\n",list[i].number);
		}
	}
	return 0;
}
