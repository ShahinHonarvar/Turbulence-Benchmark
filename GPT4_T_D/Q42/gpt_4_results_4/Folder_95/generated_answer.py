
def prime_factors(lst):
    num = lst[87]
    def prime(n):
        factor = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factor.append(i)
        if n > 1:
            factor.append(n)
        return set(factor)

    return prime(num)
