
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return {num for num in nums[8:10] if is_composite(num)}
