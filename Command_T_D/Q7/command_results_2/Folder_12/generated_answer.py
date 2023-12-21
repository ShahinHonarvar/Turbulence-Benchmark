
def all_even_ints_inclusive(lst):
    even = [x for x in lst[14:64] if x % 2 == 0]
    return even if even else []
