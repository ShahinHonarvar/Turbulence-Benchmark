def sum_of_divisors_in_range(n):
    return n*(n-1)*(n-2)//6 if n>1 and n<4 else 0
