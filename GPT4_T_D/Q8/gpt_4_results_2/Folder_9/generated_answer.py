
def all_even_ints_exclusive(integer_list):
    even_integers = []
    for i in range(71, 200):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            even_integers.append(integer_list[i])
    return even_integers
