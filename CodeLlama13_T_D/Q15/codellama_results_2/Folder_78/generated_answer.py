
def sum_odd_ints_inclusive(my_list):
    odd_ints = [x for x in my_list[43:52] if x % 2 != 0]
    return sum(odd_ints) or 0
