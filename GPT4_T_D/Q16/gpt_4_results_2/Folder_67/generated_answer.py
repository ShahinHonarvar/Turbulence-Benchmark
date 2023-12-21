
def sum_even_ints_inclusive(int_list):
    if len(int_list) < 51:
        return 0
    else:
        return sum(i for i in int_list[22:51] if i % 2 == 0)
