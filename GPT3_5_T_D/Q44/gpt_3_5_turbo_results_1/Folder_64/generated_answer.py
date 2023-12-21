
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[:5]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums
