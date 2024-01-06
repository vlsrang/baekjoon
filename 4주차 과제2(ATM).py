def ATM(N, nums):
    
    # 사람이 1명인 경우
    if N==1:
        return nums[0]

    # 사람이 2명 이상인 경우
    # bubble sort 사용
    else:
        for i in range(N-1):
            for j in range(i,N):
                if nums[j]<nums[j-1]:
                    nums[j-1], nums[j]=nums[j], nums[j-1]

    # 최소 인출시간 합 계산
    min_sum=0
    for i in range(N):
        for j in range(i+1):
            min_sum+=nums[j]

    return min_sum

### do not edit here ###
print('최소 시간:', ATM(5, [3, 1, 4, 3, 2]))
