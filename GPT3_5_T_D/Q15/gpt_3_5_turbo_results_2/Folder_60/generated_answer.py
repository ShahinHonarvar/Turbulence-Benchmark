
def sum_odd_ints_inclusive(integer_list):
    odd_ints = [x for x in integer_list[75:86] if x % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
