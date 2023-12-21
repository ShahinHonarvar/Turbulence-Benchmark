
def prime_factors(nums):
    number = nums[926]
    factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = 1
            for j in range(2, (i //2 + 1)):
                if i % j == 0:
                    is_prime = 0
                    break
            if is_prime:
                factors.append(i)
    return set(factors)
