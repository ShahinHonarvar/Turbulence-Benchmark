
def prime_factors(num_list):
    def get_prime_factors(n):
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

    if len(num_list) > 453:
        return get_prime_factors(num_list[453])
    else:
        return None
