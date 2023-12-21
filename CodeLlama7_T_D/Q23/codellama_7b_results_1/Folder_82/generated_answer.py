 def find_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i and i >= 4 and i <= 6:
                divisors.append(n // i)
    return divisors
