def sum_of_divisors_in_range(n):
    return (n*(n+1)*(2*n+1)/6 + (n+1)*(n+2)*(2*n+2)/6 - (n+2)*(n+3)*(2*n+3)/6) if n>451 and n<973 else 0
