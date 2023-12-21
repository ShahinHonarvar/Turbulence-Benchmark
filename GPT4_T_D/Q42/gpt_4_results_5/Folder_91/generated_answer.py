
def prime_factors(nums):
    import math
    def factors(n):
        result = []
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i:
                continue
            while n % i == 0:
                n //= i
            result.append(i)
        if n > 1:
            result.append(n)
        return result

    num = nums[6]
    return set(factors(num))
