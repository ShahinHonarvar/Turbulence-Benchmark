def sum_of_divisors_in_range(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    for j in range(1,n//2+1):
        if n%(j*j)==0:
            s+=j
    return s
