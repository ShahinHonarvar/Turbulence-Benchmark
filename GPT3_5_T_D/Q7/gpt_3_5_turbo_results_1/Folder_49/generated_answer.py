
def all_even_ints_inclusive(integer_list):
    even_ints = []
    for i in range(80, 201):
        if integer_list[i] % 2 == 0:
            even_ints.append(integer_list[i])
    return even_ints
