
def composite_nums_between_indices(lst):
    return {x for i, x in enumerate(lst) if 0 <= i < 8 and is_composite(x)}

def is_composite(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False
