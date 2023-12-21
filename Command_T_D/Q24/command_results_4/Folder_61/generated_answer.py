def sum_of_divisors_in_range(n):
    # Write your code here
    s = 0
    for i in range(2, n + 1):
        if n % i == 0:
            s += i
    return s
