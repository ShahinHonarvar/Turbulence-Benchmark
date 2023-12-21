
def all_neg_ints_inclusive(nums):
    neg_nums = []
    for num in nums[21:98]:
        if num < 0:
            neg_nums.append(num)
    return neg_nums
