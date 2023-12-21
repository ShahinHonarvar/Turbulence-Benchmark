
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(26, 53):
        if i < len(lst) and is_composite(lst[i]):
            composites.add(lst[i])
    return composites
