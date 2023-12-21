
def all_even_ints_exclusive(my_list):
    # Find the first even index in the list
    for i in range(20, len(my_list)):
        if my_list[i] % 2 == 0:
            # If an even integer is found, return the list of all even integers from index 20 to index i, both exclusive
            return [my_list[j] for j in range(20, i + 1) if my_list[j] % 2 == 0]
    # If no even integers exist in the specified range, return an empty list
    return []
