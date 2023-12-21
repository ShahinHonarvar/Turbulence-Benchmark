
def all_even_ints_inclusive(my_list):
    even_ints = []
    for i in range(70, 85):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
