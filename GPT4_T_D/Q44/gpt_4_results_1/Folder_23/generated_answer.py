
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i:
                continue
            else:
                return True
        return False
    composites = {n for n in lst[20:31] if is_composite(n)}
    return composites
