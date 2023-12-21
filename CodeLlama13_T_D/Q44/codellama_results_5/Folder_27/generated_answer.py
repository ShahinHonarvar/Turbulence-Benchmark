
def composite_nums_between_indices(lst):
    indices = range(22, 64)
    return {num for i, num in enumerate(lst) if i in indices and is_composite(num)}

def is_composite(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False
