
def all_even_ints_exclusive(integer_list):
    even_list = []
    for i in range(50, 74):
        if integer_list[i] % 2 == 0:
            even_list.append(integer_list[i])
    return even_list
