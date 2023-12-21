
def all_even_ints_exclusive(integer_list):
    even_ints = []
    for i in range(45, 67):
        if integer_list[i] % 2 == 0:
            even_ints.append(integer_list[i])
    return even_ints
