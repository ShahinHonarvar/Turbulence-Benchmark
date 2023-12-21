
def prime_factors(lst):
    num = lst[78]
    def factors(n):
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
        return factors

    def is_prime(n):
        if n == 1 or n == 0:
            return False
        elif n == 2:
            return True
        else:
            for x in range(2, n):
                if n % x == 0:
                    return False
            return True

    all_factors = factors(num)
    prime_factors = [factor for factor in all_factors if is_prime(factor)]
    return set(prime_factors)
