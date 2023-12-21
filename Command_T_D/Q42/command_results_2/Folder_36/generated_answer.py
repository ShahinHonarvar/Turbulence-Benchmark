def prime_factors(nums):
    res = set()
    for n in nums:
        if n == 1:
            continue
        elif n == 2:
            res.add(2)
            continue
        elif n == 3:
            res.add(3)
            continue
        for i in range(5, int(n ** .5) + 1, 6):
            if n % i == 0:
                res.add(i)
                break
        if n > 3:
            res.add(n)
    return res
