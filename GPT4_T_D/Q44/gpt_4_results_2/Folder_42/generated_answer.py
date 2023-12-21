
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    return set([num for index, num in enumerate(nums[91:100]) if is_composite(num)])
