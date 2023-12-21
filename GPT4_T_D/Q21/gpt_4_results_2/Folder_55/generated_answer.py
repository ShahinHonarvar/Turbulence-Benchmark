
def all_ints_div_by_num(int_list):
    try:
        divisible_by_two = [i for i in int_list[0:2] if i % 2 == 0]
    except IndexError:
        divisible_by_two = []
    return divisible_by_two
