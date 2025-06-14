
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(3, len(my_list)):
        if my_list[i] % 2 == 0:
            start_index = i
            break

    # Find the last even integer in the list

    for j in range(start_index, len(my_list)):
        if my_list[j] % 2 == 0:
            end_index = j
            break

    # Return a list of all even integers in the specified range

    return [my_list[k] for k in range(start_index, end_index + 1) if my_list[k] % 2 == 0]]
