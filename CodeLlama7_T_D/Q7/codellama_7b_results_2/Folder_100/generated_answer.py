
def all_even_ints_inclusive(my_list):
    start_index = 42
    end_index = 68
    even_ints = []
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
