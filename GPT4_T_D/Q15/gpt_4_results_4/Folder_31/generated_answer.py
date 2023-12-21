
def sum_odd_ints_inclusive(int_list):
    return sum(n for i,n in enumerate(int_list[75:89]) if n%2 != 0)
