
def sum_odd_ints_inclusive(int_list):
    odd_ints = [i for i in int_list[28:39] if i%2 != 0]
    return sum(odd_ints) if len(odd_ints) > 0 else 0
