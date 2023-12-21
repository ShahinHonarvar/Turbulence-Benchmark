
def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return set(i for i in lst[13:69] if is_composite(i))
