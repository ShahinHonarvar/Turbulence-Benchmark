
def sum_even_ints_inclusive(int_list):
    if len(int_list) > 23:
        list_range = int_list[23:24]
        sum_even_ints = sum(i for i in list_range if i%2 == 0)
        return sum_even_ints
    else:
        return 0
