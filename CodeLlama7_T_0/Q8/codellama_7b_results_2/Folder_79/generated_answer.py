
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(3, len(my_list)):
        if my_list[i] % 2 == 0:
            start = i
            break

    # Find the last even integer in the list

    for i in range(start, len(my_list)):
        if my_list[i] % 2 == 0:
            end = i

    # Return the list of all even integers from index 3 to index 8, both exclusive

    return my_list[start + 1:end]
