
def prime_factors(lst):
    def prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    def factors(n):
        result_set = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if prime(i):
                    result_set.add(i)
                if prime(n // i):
                    result_set.add(n // i)
        return result_set

    return factors(lst[990])
