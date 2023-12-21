
def composite_nums_between_indices(list_nums):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return set([i for i in list_nums[527:539] if is_composite(i)])
