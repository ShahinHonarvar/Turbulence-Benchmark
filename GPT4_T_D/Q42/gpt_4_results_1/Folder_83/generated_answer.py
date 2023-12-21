
def prime_factors(nums):
    def factors(n):
        factors = set()
        for i in range(2, n+1):
            if n % i == 0:
                is_prime = True
                for num in range(2, i):
                    if i % num == 0:
                        is_prime = False
                if is_prime:
                    factors.add(i)
        return factors

    return factors(nums[95])
