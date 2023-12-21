import sys
def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    for i in range(48, 62):
        if i * i <= n:
            divisors.append(i)
            for j in range(i + 1, n // i + 1):
                divisors.append(i * j)
    return divisors
