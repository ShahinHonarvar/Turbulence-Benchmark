
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for num in nums[:5]:
        if is_composite(num):
            composite_nums.add(num)
    
    return composite_nums
