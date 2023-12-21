
def all_even_ints_exclusive(my_list):
    even_ints = []
    for i in range(42, 87):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
