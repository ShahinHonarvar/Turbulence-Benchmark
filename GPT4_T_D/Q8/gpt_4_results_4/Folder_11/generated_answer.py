
def all_even_ints_exclusive(list_of_ints):
    list_in_range = list_of_ints[16:99]
    even_numbers = [num for num in list_in_range if num % 2 == 0]
    return even_numbers
