
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    return_set = set()
    for i in range(42, 69):
        if i < len(lst) and is_composite(lst[i]):
            return_set.add(lst[i])

    return return_set
