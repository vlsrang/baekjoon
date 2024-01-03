def score_average():
    print("성적을 입력하세요. :")

    summ=[]
    count=0
    while True:
        sc=input("점수(0~100) : ")

        if sc!='q':
        
            while not (sc.isdigit()==True):
                sc=input("%형식 오류% 점수(0~100) : ")

            while not (int(sc)>=0 and int(sc)<=100):
                sc=input("%범위 오류% 점수(0~100) : ")

            if sc:
                summ.append(int(sc))
                count+=1
                continue
        if str(sc)=="q":
            avg=sum(summ)/len(summ)
            print("%d 과목 평균 성적 : %.1f"%(count,avg))
            break
    
    
##### do not edit here #####
score_average()
