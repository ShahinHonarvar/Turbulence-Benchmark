
def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 42:
        return []
    x = numbers[41]

    import sympy

    primes = []
    for number in range(2, x+1):
        if sympy.isprime(number) and '0' not in str(number):
            while str(number) and sympy.isprime(int(str(number))):
                number = str(number)[1:-1]
            if not str(number):
                primes.append(number)
    return sorted(primes, reverse=True)
