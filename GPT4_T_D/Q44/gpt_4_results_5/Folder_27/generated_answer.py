
def composite_nums_between_indices(nums):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(22, min(64, len(nums))):
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites
