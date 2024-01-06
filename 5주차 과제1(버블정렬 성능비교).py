import time

bList=[]
while True:
    sc=input("숫자 입력: ")

    if sc != 'n' and sc != 'N' :
        
        while not (sc.isdigit()==True):
            sc=input("숫자 입력: ")

        if sc:
            bList.append(int(sc))
            continue
    if str(sc)=="n" or str(sc)=="N":
        break
N = len(bList)

start1=time.time()
for i in range(N-1):
    for j in range(N-1):
        if bList[j]>bList[j+1]:
            bList[j], bList[j+1]=bList[j+1], bList[j]
 
print(bList)
print("time :", time.time() - start1)

start2=time.time()
for i in range(N-1):
    change=False
    for j in range(N-1):
        if bList[j]>bList[j+1]:
            bList[j], bList[j+1]=bList[j+1], bList[j]
            change=True
    if change==False:
        break
 
print(bList)
print("time :", time.time()-start2)

start3=time.time() 
def bub(bList):
    flag=0
    for i in range(len(bList)-1):
        if bList[i] > bList[i+1]:
            flag=1
            bList[i], bList[i+1] = bList[i+1], bList[i]
    if flag==0:
        return print(bList)
    else:
        return bub(bList)

  
bub(bList)
print(bList)
print("time :", time.time() - start3)
