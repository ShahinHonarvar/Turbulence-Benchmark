
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(23, min(24, len(lst))):
        if is_composite(lst[i]):
            composites.add(lst[i])
    return composites
