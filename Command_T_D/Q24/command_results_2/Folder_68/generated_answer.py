def sum_of_divisors_in_range(n):
    return n*n*n//6 + (n-1)*n*(n-2)//6 + (n-2)*(n-3)/6
