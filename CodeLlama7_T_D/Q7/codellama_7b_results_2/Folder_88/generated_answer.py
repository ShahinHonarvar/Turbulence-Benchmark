
def all_even_ints_inclusive(my_list):
    # Find the index of the first even integer in the list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            first_even_index = i
            break

    else:

        # If no even integers are found, return an empty list

        return []

    # Find the index of the last even integer in the list

    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] % 2 == 0:
            last_even_index = i
            break

    # Return the list of all even integers from index 4 to index 8, both inclusive

    return my_list[first_even_index:last_even_index+1]
