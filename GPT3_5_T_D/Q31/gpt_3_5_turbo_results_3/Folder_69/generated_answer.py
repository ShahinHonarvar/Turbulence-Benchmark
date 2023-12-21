
def if_perfect_num(nums):
    return sum([i for i in range(1, int(nums[459]/2) + 1) if nums[459] % i == 0]) == nums[459]
