
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    res = set()
    for i in range(29, min(79, len(lst) - 1) + 1):
        if is_composite(lst[i]):
            res.add(lst[i])
    return res
