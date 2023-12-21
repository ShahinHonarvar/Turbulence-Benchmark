
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**(0.5)) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = {num for i, num in enumerate(nums[42:69]) if is_composite(num)}
    return composite_nums
