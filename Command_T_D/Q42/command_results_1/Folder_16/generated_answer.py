def prime_factors(nums):
    res = set()
    for i in nums:
        if i == 162:
            continue
        for j in range(2, int(i**(0.5))+1):
            if i % j == 0:
                res.add(j)
                break
            elif j*j != i:
                res.add(i)
                break
    return res
