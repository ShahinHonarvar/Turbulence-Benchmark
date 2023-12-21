
def prime_factors(lst):
    def factors(n):
        i = 2
        factors = set()
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.add(i)
        if n > 1:
            factors.add(n)
        return factors

    try:
        return factors(lst[47])
    except IndexError:
        return "Error: Index out of range"
