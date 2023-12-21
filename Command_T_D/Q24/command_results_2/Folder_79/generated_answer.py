def sum_of_divisors_in_range(n):
    return n*n*n*(n-1)*(n-2)*(n-3)*(n-4)*(n-5)*(n-6)*(n-7) if n<=8 else 0
