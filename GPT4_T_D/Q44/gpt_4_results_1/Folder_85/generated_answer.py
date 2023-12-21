
def composite_nums_between_indices(nums):
    def is_composite(num):
        factors = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factors += 1
            if factors > 2:
                return True
        return False

    composite_nums = set()
    for num in nums[3:6]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums
