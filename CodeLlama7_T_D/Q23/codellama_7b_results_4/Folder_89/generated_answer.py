
def find_divisors_in_range(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return [divisor for divisor in divisors if 14 <= divisor <= 48]
