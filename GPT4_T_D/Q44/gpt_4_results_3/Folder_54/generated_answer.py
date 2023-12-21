
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
        
    return {n for i, n in enumerate(nums[14:65]) if is_composite(n)}
