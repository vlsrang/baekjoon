S = [5, 2, 3, 4, 6]  

def matrix_chain(S):
    size = len(S) -1
    matrix=[]
    for p in range(size):
        matrix.append([S[p],S[p+1]])
    dp=[[0]*size for _ in range(size)]

    for i in range(1,size):
        for j in range(0,size-i):
            if i == 1: 
                dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
                continue
        
            dp[j][j+i] = 2**32 
            for k in range(j, j+i): 
                dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])

    return dp[0][size-1]
    
print("The minimum number of operations =", matrix_chain(S))
