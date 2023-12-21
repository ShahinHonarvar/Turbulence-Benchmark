def all_left_truncatable_prime(nums):
    res = []
    for i in range(nums[85] // 10):
        s = str(10 ** i)
        while s:
            p = int(s)
            if all(p % d == 0 for d in range(2, int(s[0]))) and p in nums and p not in res:
                res.append(p)
            s = s[1:]
    return sorted(res)
