
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return True
            return False
        return False

    return {num for i, num in enumerate(nums[60:201]) if is_composite(num)}
