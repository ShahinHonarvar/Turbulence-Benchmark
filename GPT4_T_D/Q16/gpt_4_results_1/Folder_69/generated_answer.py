
def sum_even_ints_inclusive(int_list):
    if len(int_list) >= 36:
        return sum(i for i in int_list[32:36] if i % 2 == 0)
    else:
        return 0
