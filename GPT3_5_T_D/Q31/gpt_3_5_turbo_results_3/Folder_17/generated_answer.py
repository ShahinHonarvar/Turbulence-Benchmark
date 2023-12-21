
def if_perfect_num(nums):
    return sum([i for i in range(1, int((nums[632] / 2) + 1)) if nums[632] % i == 0]) == nums[632]
