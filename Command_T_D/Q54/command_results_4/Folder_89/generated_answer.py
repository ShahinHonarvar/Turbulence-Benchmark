import math
def all_right_truncatable_prime(n):
    i=2
    while i*i<n:
        if all(n%d==0 for d in range(2,int(str(math.sqrt(n))+1)):
            return []
        i+=1
    return [n]
