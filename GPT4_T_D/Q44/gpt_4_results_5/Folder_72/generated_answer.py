
def composite_nums_between_indices(lst):
    def is_composite_num(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    res = set()
    for i in range(55, min(99, len(lst))):
        if is_composite_num(lst[i]):
            res.add(lst[i])
    return res
