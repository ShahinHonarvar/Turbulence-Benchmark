
def all_even_ints_inclusive(my_list):
    return [i for i in my_list if i % 2 == 0 and 0 <= i <= len(my_list) - 1]
