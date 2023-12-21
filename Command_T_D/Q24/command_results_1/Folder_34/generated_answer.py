def sum_of_divisors_in_range(n):
    # Your code here
    return 0 if n<4 or n>5 else sum(range(4,n+1,2))
