
def prime_factors(nums):
    num = nums[0]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                factors.add(i)
    return factors
