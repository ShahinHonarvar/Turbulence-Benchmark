
def prime_factors(lst):
    def factors(n):
        i = 2
        factors_set = set()
        while i <= n:
            if (n % i) == 0:
                factors_set.add(i)
                n = n // i
            else:
                i = i + 1
        return factors_set

    idx_78 = lst[78]
    return factors(idx_78)
