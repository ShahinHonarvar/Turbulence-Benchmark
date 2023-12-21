
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(62, 79):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])

    return composite_nums
