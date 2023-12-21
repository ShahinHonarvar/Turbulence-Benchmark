
def all_even_ints_exclusive(my_list):
    # Get the range of even integers from index 48 to index 76, both exclusive
    even_ints = []
    for i in range(48, 76):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
