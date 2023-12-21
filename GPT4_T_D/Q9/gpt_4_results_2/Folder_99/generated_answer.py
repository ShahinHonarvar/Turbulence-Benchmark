
def all_odd_ints_inclusive(lst):
    sublist = lst[310:371]
    odd_ints = [num for num in sublist if num % 2 != 0]
    return odd_ints
