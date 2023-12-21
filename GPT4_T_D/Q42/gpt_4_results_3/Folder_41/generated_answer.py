
def prime_factors(nums):
    def prime_fact(n):
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
        return prime_fact(nums[84])
    except IndexError:
        return "List index out of range"
