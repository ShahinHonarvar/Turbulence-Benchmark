
def composite_nums_between_indices(nums):
    def is_composite(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for index in range(32, 36):
        if is_composite(nums[index]):
            composite_nums.add(nums[index])

    return composite_nums
