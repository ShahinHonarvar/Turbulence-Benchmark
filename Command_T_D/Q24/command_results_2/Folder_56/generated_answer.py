def sum_of_divisors_in_range(n):
    # Your code here
    if n <= 7:
        return 0
    else:
        return sum(range(6, n//2 + 1))
