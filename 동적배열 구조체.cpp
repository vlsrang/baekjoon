#include <stdio.h>
#include <stdlib.h>

struct Student{
	int student_id, grade;
	char name[10];
};

int main(){
	struct Student *ptr;
	int num=0, i=0;
	
	printf("�л����� �Է��ϼ���: ");
	scanf("%d", &num);
	
	ptr=(struct Student*)malloc(num*sizeof(struct Student));
	
	for (i=0;i<num;i++){
		printf("%d��° �л� �й��� �Է��ϼ���:",i+1);
		scanf("%d",&ptr[i].grade);
		printf("%d��° �л� �̸��� �Է��ϼ���:",i+1);
		scanf("%s",ptr[i].name);
		printf("%d��° �л� ������ �Է��ϼ���:",i+1);
		scanf("%d",&ptr[i].student_id);
	};
	
	for (i=0;i<num;i++){
		printf("�й�: %d \t �̸�: %s \t ����: %d\n",ptr[i].grade,ptr[i].name,ptr[i].student_id);

		
	};
	return 0;	
}
