
def prime_factors(nums):
    num = nums[714]
    factors = []
    for i in range(2, num+1):
        if num % i == 0:
            prime = True
            for j in range(2, int(i**(0.5)) + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                factors.append(i)
    return set(factors)
