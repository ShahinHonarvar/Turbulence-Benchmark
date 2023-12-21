
def composite_nums_between_indices(lst):
    if len(lst) == 0:
        return set()
    else:
        start, end = max(222, min(len(lst), 222)), min(len(lst), 222) + 1
        return {x for x in lst[start:end] if not is_prime(x)}
