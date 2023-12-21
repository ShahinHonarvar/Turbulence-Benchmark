
def all_even_ints_exclusive(int_list):
    sub_list = int_list[16:40]
    even_ints = [num for num in sub_list if num % 2 == 0]
    return even_ints
