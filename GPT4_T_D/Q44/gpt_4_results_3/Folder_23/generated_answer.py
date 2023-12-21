
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_nums = []
    for i in range(20, 31):
        if i < len(lst) and is_composite(lst[i]):
            composite_nums.append(lst[i])
    return set(composite_nums)
