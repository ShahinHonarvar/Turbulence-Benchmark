def sum_of_divisors_in_range(n):
    divisor_sieve = set()
    for i in range(2, n // 2):
        if not divisor_sieve:
            break
        if n % i == 0:
            divisor_sieve.add(i)
            if i * i != n:
                divisor_sieve.add(n // i)
    divisor_sieve.add(n)
    return sum(divisor_sieve)
