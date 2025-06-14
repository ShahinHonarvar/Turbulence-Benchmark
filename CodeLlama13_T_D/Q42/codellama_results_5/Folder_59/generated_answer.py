
def prime_factors(nums):
    result = set()
    for num in nums:
        i = 2
        while i * i <= num:
            if num % i == 0:
                result.add(i)
            i += 1
    return result
