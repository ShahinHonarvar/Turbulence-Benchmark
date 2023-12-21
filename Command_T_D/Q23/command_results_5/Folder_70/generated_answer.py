import sys
def find_divisors_in_range(n):
    lst = []
    for x in range(5,n//2+1):
        if x*x<=n:
            if n%x==0:
                lst.append(x)
            for y in range(x*x,n//x):
                if n%y==0:
                    lst.append(y)
    if n%2==0:
        lst.append(n//2)
    return lst
