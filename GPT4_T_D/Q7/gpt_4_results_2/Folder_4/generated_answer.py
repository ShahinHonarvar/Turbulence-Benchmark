
def all_even_ints_inclusive(integer_list):
    selected_range = integer_list[12:93]
    even_integers = [num for num in selected_range if num % 2 == 0]
    return even_integers
