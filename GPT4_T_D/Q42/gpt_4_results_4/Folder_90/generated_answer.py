
def prime_factors(lst):
    def prime_facts(n):
        i, factors = 2, []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return set(factors)
    return prime_facts(lst[263])
