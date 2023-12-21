
def all_even_ints_inclusive(integer_list):
    even_numbers = []
    for i in range(37, 52):
        if integer_list[i] % 2 == 0:
            even_numbers.append(integer_list[i])
    return even_numbers
