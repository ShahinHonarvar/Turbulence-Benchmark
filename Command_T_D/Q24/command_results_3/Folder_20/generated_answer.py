def sum_of_divisors_in_range(n):
    if n < 28 or n > 81:
        return 0
    # find all divisors of n in range (28,81]
    # we can assume that n is a prime number
    divisor_set = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_set.add(i)
            if i * i != n:
                divisor_set.add(n // i)
    # sum of all divisors in range (28,81]
    return sum(divisor_set)
