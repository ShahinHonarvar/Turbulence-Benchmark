
def all_even_ints_exclusive(my_list):
    return [i for i in my_list if i % 2 == 0 and i < len(my_list) - 1]
