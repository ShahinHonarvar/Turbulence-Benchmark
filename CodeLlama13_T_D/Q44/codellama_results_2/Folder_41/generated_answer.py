
def composite_nums_between_indices(nums):
    return {x for i, x in enumerate(nums) if 0 <= i < 3 and is_composite(x)}

def is_composite(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
