
def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 1 <= i <= 8 and is_composite(num)}

def is_composite(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False
