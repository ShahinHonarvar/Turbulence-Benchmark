
def prime_factors(integer_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = set()
        i = 2
        while i <= n:
            if n % i == 0:
                factors.add(i)
                n //= i
            else:
                i += 1
        return factors

    return get_prime_factors(integer_list[247])
