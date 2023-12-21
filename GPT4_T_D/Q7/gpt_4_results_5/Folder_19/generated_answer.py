
def all_even_ints_inclusive(lst):
    sublist = lst[3:6]
    even_nums = [i for i in sublist if i % 2 == 0]
    return even_nums
