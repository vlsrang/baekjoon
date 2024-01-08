def binary_search(arr, score):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == score:
            return mid+1
        elif arr[mid] > score:
            end = mid - 1
        else:
            start = mid + 1
    rank = mid + 1
    return rank

import os
f = open('C:/data/score.txt','r',encoding='UTF-8')
scores=[]
sc=f.readlines()
for i in range(len(sc)):
    scores.append(float(sc[i]))
for i in range(len(scores)):
    for j in range(len(scores)-1,i,-1):
        if scores[j]>scores[j-1]:
            scores[j], scores[j-1]=scores[j-1], scores[j]


f.close()

my_score = 81
rank = binary_search(scores, my_score)
print(f'{my_score}점은 {rank}등 입니다')
