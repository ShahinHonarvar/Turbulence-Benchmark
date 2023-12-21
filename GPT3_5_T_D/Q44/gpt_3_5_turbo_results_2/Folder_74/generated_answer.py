
def composite_nums_between_indices(nums):
    def isComposite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(42, 69):
        if isComposite(nums[i]):
            composites.add(nums[i])

    return composites
