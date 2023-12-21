
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n): 
            if n % i == 0:
                return True
        return False

    composites = set()
    for num in nums[1:6]:
        if is_composite(num):
            composites.add(num)
    return composites
