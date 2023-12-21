
def all_left_right_truncatable_prime(nums):
    res = []
    for num in nums:
        if num >= 100:
            break
        for x in range(num, 0, -1):
            if x == 2:
                continue
            if all(int(d) for d in str(x)):
                res.append(x)
                break
    return res
