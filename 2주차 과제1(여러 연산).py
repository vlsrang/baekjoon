def data_describe(fname):

    def load_data(fname):
        import os
        f=open('C:/data/week_1_1.txt','r',encoding='UTF-8')
        data=[]
        for line in f.read().splitlines():
            if line.isdigit()==True:
                if int(line)>=1:
                    data.append(line)
        
        return data # 숫자만 포함된 리스트 

    def get_mean():
        summ=0
        for i in data:
            summ+=int(i)
            mean=float(summ/len(data))

        return mean

    def get_std(mean):  #  input 수정가능 (선택)
                        # return: std # 데이터의 표준편차
        import math
        vsum=0
        for x in data:
            vsum=vsum+(int(x)-mean)**2
        var=vsum/len(data)
        std=math.sqrt(var)
        

        return math.sqrt(var)

    def sort_values():
        num=len(data)
        for i in range(num):
            for j in range(i,num):
                if data[j]<data[i]:
                    data[j], data[i]=data[i],data[j]

    def get_median():
        num=len(data)
        median_idx=num//2

        return data[median_idx]

    def get_max():
   
        return data[-1]
        
    def get_min():

        return data[0]

    ####### do not edit here
    ###### 함수 실행 순서에 유의하세요.
    data = load_data(fname)
    mean = get_mean()
    std = get_std(mean)
    sort_values()
    median = get_median()
    max = get_max()
    min = get_min()

    print(f"""
    count = {len(data)}
    mean = {mean}
    median = {median}
    std = {std}
    max = {max}
    min = {min}
    """)
