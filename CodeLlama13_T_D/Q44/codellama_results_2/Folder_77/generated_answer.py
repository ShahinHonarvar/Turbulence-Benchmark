
def composite_nums_between_indices(lst):
    start, end = 667, 774
    return {x for x in lst[start:end+1] if is_composite(x)}

def is_composite(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
