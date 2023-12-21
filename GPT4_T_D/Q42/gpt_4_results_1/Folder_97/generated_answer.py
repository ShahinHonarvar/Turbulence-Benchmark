
def prime_factors(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def factors(n):
        fctrs = set()
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            if is_prime(i):
                fctrs.add(i)
            if is_prime(n // i):
                fctrs.add(n // i)
        return fctrs

    try:
        return factors(lst[132])
    except IndexError:
        return "The list does not have 133 elements."
