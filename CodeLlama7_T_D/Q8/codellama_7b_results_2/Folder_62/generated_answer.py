
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list, starting from index 55
    for i in range(55, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    # Find the last even integer in the list, ending at index 84

    for i in range(start_index, len(my_list) - 1):
        if my_list[i] % 2 == 0:
            end_index = i
            break

    # Return the list of all even integers between start_index and end_index, both exclusive

    return my_list[start_index + 1 : end_index]
