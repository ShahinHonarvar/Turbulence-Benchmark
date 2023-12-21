
def sum_even_ints_inclusive(int_list):
    try:
        sub_list = int_list[23:24]
        even_sum = sum(i for i in sub_list if i % 2 == 0)
        return even_sum
    except IndexError:
        return 0
