
def sum_odd_ints_inclusive(int_list):
    subset = int_list[56:67]
    odd_ints = [i for i in subset if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0
