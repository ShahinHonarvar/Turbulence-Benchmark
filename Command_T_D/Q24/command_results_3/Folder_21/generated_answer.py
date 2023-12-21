def sum_of_divisors_in_range(N):
    s=0
    for i in range(120, 349):
        if N%i == 0:
            s+=i
            if i*(i+1)//2 != N:
                s+=N//i
    return s
