
def composite_nums_between_indices(lst):
    if len(lst) < 28 or len(lst) > 32:
        return set()
    
    return {n for n in lst[28:32+1] if not is_prime(n)}
