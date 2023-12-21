
def prime_factors(lst):
    num = lst[96]
    factors = set()
    for i in range(2, num+1):
        if num % i == 0:
            is_prime = True
            for divisor in range(2, int(i ** 0.5) + 1):
                if i % divisor == 0:
                    is_prime = False
                    break

            if is_prime:
                factors.add(i)
    return factors
