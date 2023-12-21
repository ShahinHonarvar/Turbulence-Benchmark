
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 4:
            return False
        if n % 2 == 0:
            return True
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(30, 49):
        if is_composite(lst[i]):
            composites.add(lst[i])

    return composites
