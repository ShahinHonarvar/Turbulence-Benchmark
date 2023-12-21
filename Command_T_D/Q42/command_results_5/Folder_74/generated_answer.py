def prime_factors(nums):
    factors = set()
    for num in nums:
        if num == 1:
            continue
        elif num == 2:
            factors.add(2)
            continue
        elif num == 3:
            factors.add(3)
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.add(i)
                break
            else:
                factors.add(num)
                break
    return factors
