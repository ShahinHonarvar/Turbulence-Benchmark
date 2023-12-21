
def prime_factors(nums):
    number = nums[40]
    factors = set()
    i = 2
    while number > 1:
        if number % i == 0:
            factors.add(i)
            number = number // i
        else:
            i += 1
    return factors
