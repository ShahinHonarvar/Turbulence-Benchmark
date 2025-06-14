
def all_ints_not_div_by_num(my_list):
    # Find the first index where the integer is not divisible by 593
    first_index = next((i for i, x in enumerate(my_list) if x % 593 != 0), len(my_list))
    # Find the last index where the integer is not divisible by 593
    last_index = next((i for i, x in enumerate(my_list[::-1]) if x % 593 != 0), len(my_list))
    return my_list[first_index:last_index]
