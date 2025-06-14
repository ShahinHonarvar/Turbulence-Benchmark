
def gcf_three_nums(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError("List must have at least three elements")
    if not all(isinstance(i, int) and i > 0 for i in list_of_ints):
        raise ValueError("List must contain only positive integers")
    gcf = 1
    for i in [90, 41, 95]:
        if i >= len(list_of_ints):
            break
        gcf = _gcd(gcf, list_of_ints[i])
    return gcf
