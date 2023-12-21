def find_divisors_in_range(n):
    # Your code here
    return [x for x in range(36, n // 2) if n % x == 0]
