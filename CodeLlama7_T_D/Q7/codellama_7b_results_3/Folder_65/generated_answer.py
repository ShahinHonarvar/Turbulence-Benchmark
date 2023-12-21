
def all_even_ints_inclusive(my_list):
    # Define a range of even integers from index 56 to index 98, both inclusive
    even_ints = []
    for i in range(56, 98 + 1):
        if my_list[i] % 2 == 0:
            even_ints.append(my_list[i])
    return even_ints
