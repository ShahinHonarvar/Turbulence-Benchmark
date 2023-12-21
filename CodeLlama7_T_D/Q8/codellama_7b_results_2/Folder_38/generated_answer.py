
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(15, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i + 1
            break

    # Find the last even integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] % 2 == 0:
            end = i - 1
            break

    # Return the list of all even integers from index 15 to index 40, both exclusive

    return my_list[start:end]
