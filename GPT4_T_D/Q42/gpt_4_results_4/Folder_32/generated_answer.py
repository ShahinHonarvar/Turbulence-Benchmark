
def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_div = int(n ** 0.5) + 1
        for div in range(3, max_div, 2):
            if n % div == 0:
                return False
        return True

    def factors(n):
        factors_set = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_prime(i):
                    factors_set.add(i)
                if is_prime(n//i):
                    factors_set.add(n//i)
        return factors_set

    return factors(numbers[849])
