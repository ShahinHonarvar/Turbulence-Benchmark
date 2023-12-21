
def sum_even_ints_inclusive(list_of_ints):
    list_range = list_of_ints[111:112]
    even_ints = [num for num in list_range if num % 2 == 0]
    return sum(even_ints) if even_ints else 0
