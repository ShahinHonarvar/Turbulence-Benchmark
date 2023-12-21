
def all_even_ints_inclusive(int_list):
    sub_list = int_list[12:93]
    even_list = [i for i in sub_list if i%2 == 0]
    return even_list
