
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num <= 1:
            return False
        for factor in range(2, num):
            if num % factor == 0:
                return True
        return False
    
    return {num for num in nums[:4] if is_composite(num)}
