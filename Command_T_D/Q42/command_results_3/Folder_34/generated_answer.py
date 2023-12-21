def prime_factors(nums):
    if len(nums) == 0:
        return set()
    a, b, res = nums[0], nums[0], set()
    while a:
        if a == b:
            break
        elif a == b + 1:
            continue
        elif a == b - 1:
            res.add(a)
            break
        elif a % b == 0:
            res.add(b)
            break
        else:
            res.add(a)
            break
        a += 1
        b += 1
    return res
