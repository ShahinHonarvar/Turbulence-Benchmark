
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(50, len(my_list), 2):
        if my_list[i] % 2 == 0:
            # Start building the output list
            output = [my_list[i]]

    # Find all even integers in the specified range
    for i in range(50, 92, 2):
        if my_list[i] % 2 == 0:
            output.append(my_list[i])

    return output
