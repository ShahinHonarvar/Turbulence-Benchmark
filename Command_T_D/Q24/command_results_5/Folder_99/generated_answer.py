def sum_of_divisors_in_range(n):
    return (n*(n+1)*(2*n+1))//6 if n in range(378, 782) else 0
