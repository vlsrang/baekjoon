#include <stdio.h>
#include <stdlib.h>

struct Student{
	int student_id, grade;
	char name[10];
};

int main(){
	struct Student *ptr;
	int num=0, i=0;
	
	printf("학생수를 입력하세요: ");
	scanf("%d", &num);
	
	ptr=(struct Student*)malloc(num*sizeof(struct Student));
	
	for (i=0;i<num;i++){
		printf("%d번째 학생 학번을 입력하세요:",i+1);
		scanf("%d",&ptr[i].grade);
		printf("%d번째 학생 이름을 입력하세요:",i+1);
		scanf("%s",ptr[i].name);
		printf("%d번째 학생 학점을 입력하세요:",i+1);
		scanf("%d",&ptr[i].student_id);
	};
	
	for (i=0;i<num;i++){
		printf("학번: %d \t 이름: %s \t 학점: %d\n",ptr[i].grade,ptr[i].name,ptr[i].student_id);

		
	};
	return 0;	
}
