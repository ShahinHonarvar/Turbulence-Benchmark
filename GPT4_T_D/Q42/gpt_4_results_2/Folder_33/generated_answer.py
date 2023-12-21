
def prime_factors(int_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n):
        factors = set()
        for i in range(1, int(n**(0.5)) + 1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
        return factors

    if len(int_list) > 321:
        num = int_list[321]
        factors = get_factors(num)
        prime_factors = set(filter(is_prime, factors))
        return prime_factors
    else:
        return set()
