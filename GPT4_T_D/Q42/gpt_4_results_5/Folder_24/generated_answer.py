
def prime_factors(int_list):
    def factorize(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return set(factors)

    if len(int_list) > 74:
        return factorize(int_list[74])
