
def prime_factors(lst):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def factors(n):
        facs = set()
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            if is_prime(i):
                facs.add(i)
            if is_prime(n // i):
                facs.add(n // i)
        return facs
    return factors(lst[21])
