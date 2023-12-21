
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    nums = set()
    for i in range(min(10, len(lst))):
        if is_composite(lst[i]):
            nums.add(lst[i])
    return nums
