def sosu(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:      
        for i in range(2,n):
            if n%i==0:
                return False
        return True

def sum_sosu(m,n):
    def loop(m,n,sum):
        if m<=n:
            if sosu(m):
                return loop(m+1,n,m+sum)
            else:
                return loop(m+1,n,sum)
        else:
            return sum
                

    return loop(m,n,0)

### do not edit here ###
print('결과:',sum_sosu(1,10))


"""
def sosu(n):
    if n<=1:
        return False
    else:      
        for i in range(2,n):
            if n%i==0:
                return False
    return True

def sum_sosu(m,n):
    def loop(m,n,sum):
        if m>n:
            return sum
        else:
            if sosu(m)==True:
                sum+=m
            return loop(m+1,n,sum)
                

    return loop(m,n,0)
"""
