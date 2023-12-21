def prime_factors(nums):
    fac = set()
    for i in nums:
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                fac.add(j)
                i = i // j
                break
        if i > 1:
            fac.add(i)
    return fac
