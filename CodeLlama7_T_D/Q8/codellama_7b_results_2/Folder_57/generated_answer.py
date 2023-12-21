
def all_even_ints_exclusive(my_list):
    # Find the first even index in the list
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            first_even = i
            break

    # If no even indices exist, return an empty list
    if first_even is None:
        return []

    # Find the last even index in the list
    for i in range(len(my_list) - 1, first_even, -1):
        if my_list[i] % 2 == 0:
            last_even = i
            break

    # Return the list of all even integers from index 18 to index 37, both exclusive
    return my_list[first_even + 18:last_even + 18]
