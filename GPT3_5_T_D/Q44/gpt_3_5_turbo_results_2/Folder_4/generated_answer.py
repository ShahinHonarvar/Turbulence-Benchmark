
def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(56, 99):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums

def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False
