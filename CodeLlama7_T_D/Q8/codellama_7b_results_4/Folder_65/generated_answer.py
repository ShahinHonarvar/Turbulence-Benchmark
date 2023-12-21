
def all_even_ints_exclusive(my_list):
    # Find the first even index in the range
    for i in range(42, len(my_list), 1):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    # Find the last even index in the range

    for i in range(start_index, len(my_list), 1):
        if my_list[i] % 2 == 0:
            end_index = i
            break

    # Return a list of all even integers in the specified range

    return [my_list[i] for i in range(start_index, end_index + 1, 1) if my_list[i] % 2 == 0]]
