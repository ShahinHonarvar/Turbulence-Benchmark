import sys
def sum_of_divisors_in_range(n):
    #sys.setrecursionlimit(10**6)
    if n<=10 or n>=42:
        return 0
    res=0
    for i in range(11,41):
        if n%i==0:
            res+=i
            if i*i!=n:
                res+=n//i
    return res
