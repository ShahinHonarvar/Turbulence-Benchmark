
def prime_factors(lst):
    num = lst[74]
    def get_factors(n):
        factors = set()
        for i in range(2, n+1):
            while n % i == 0:
                factors.add(i)
                n = n / i
        return factors
    return get_factors(num)
