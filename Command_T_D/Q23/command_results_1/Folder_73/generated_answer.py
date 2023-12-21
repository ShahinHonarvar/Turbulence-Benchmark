def find_divisors_in_range(n):
    # your code here
    if n < 46 or n > 89:
        return []
    divisor = []
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i * i != n:
                divisor.append(n // i)
    return sorted(set(divisor))
