
def all_even_ints_exclusive(my_list):
    # Find the first even index in the list
    for i in range(28, len(my_list), 2):
        if my_list[i] % 2 == 0:
            return my_list[i+1::2]
    # If no even integers exist in the specified range, return an empty list
    return []
