
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return True
        return False

    if len(lst) < 52:
        upper_bound = len(lst)
    else:
        upper_bound = 52

    return {n for n in lst[37:upper_bound] if is_composite(n)}
