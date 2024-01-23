import numpy as np

def get_integer(message, a, b):
    n = input(message)
    if b == None:
        while not((n[0]=='-' and n[1:].isdigit()) or n.isdigit() and int(n)>=a):
            n = input(message)
    else:
        while not((n[0]=='-' and n[1:].isdigit()) or n.isdigit() and int(n)>=a and int(n)<=b):
            n = input(message)
    return int(n)
                  
def print_score(score):  #학생 점수 출력 기능
    print("\n학생 수는 %d명 입니다."%n)
    num=get_integer("학생의 번호를 입력하세요.:",1,n)
    print("%d의 점수 : %s"%(num, score[num-1]))
          
def fix_score(score):  #학생의 점수 수정 기능
    print("\n학생 수는 %d명 입니다."%n)
    num=get_integer("학생의 번호를 입력하세요.:",1,n)
    print("%d의 점수 : %s"%(num, score[num-1]))
    print("수정할 점수를 입력하세요.\n -1을 입력하면 점수는 유지됩니다.")

    subject=['국어','수학','영어','한국사']
    for i in range(4):
        print("%s 점수: "%subject[i],end='')
        sc=get_integer(subject[i]+"의 점수 :",-1,100)
        if sc != -1:
            score[num-1][i]=sc     

def stats_subject(score):  #과목별 평균, 분산 보기 기능
    print('')
    score=score.transpose()
    subject=['국어','수학','영어','한국사']
    for i in range(4):
        print(subject[i]+"평균: %.2f"%np.mean(score[i]),end=' ')
        print(subject[i]+"분산: %.2f"%np.var(score[i]))
    score=score.transpose()

def stats_student(score):  #학생별 평균, 분산 계산 기능
    print("\n0을 입력하면 학생 번호 입력이 종료됩니다.")
    student=[]
    while True:
        num=get_integer("학생의 번호를 입력하세요.: ",0,n)
        if num==0:
            break
        else:
            student.append(num)
    student=list(set(student))
    for num in student:
        print("%d의 점수: "%num, end='')
        print(score[num-1])

    size=len(student)
    if size!=0:
        mini=score[student[0]-1]
        cnt=1
        while cnt<size:
            mini=np.concatenate((mini,score[student[cnt]-1]))
            cnt+=1
        mini=mini.reshape(size,4)
        avg=np.mean(mini,axis=0)
        var=np.var(mini,axis=0)
        subject=['국어','수학','영어','한국사']
        for i in range(4):
            print(subject[i]+"평균: %.2f"%avg[i],end=' ')
            print(subject[i]+"분산: %.2f"%var[i])

##### do not edit here #####
n = get_integer("학생 수를 입력하세요. : ", 1, None)
                  
score = np.random.randint(0, 101, (n, 4))
                  
while True:
    print("\n<메뉴>")
    print("1. 학생의 점수 출력")
    print("2. 학생의 점수 수정")              
    print("3. 과목별 평균, 분산 보기")              
    print("4. 학생별 평균, 분산 계산")              
    print("0. 종료")              
    ch = get_integer("할 일의 번호를 선택하세요. : ", 0, 4)
                  
    if ch == 1:
        print_score(score)
    elif ch == 2:
        fix_score(score)
    elif ch == 3:
        stats_subject(score)
    elif ch == 4:
        stats_student(score)
    else:
        break
