
def composite_nums_between_indices(nums):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composites = set()
    for i in range(62, min(len(nums), 100)):
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites
