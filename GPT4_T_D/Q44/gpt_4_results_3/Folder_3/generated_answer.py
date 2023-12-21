
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_set = set()
    for i in range(66, 94):
        if i < len(lst) and is_composite(lst[i]):
            composite_set.add(lst[i])
    return composite_set
