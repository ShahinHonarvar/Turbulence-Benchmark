
def if_perfect_num(nums):
    if len(nums) > 76:
        n = nums[77]
        s = sum(filter(lambda x: x < n and n % x == 0, range(1, int(n**0.5) + 1)))
        return s == n
    else:
        return False
