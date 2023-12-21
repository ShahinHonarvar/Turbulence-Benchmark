
def all_even_ints_inclusive(my_list):
    # Get the range of even integers from index 75 to index 85, both inclusive
    even_ints = []
    for i in range(75, 86):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
