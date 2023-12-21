
def all_left_right_truncatable_prime(nums):
    res = []
    for i in range(2, int(str(nums[55])[0]) + 1):
        s = str(i)
        while len(s) > 1:
            s = s[:-1] + s[-1:]
            if all(int(i) == i for i in s):
                res.append(int(s))
    return res
