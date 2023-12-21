
def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composite_set = set()
    for num in lst[0:7]:
        if is_composite(num):
            composite_set.add(num)
    return composite_set
