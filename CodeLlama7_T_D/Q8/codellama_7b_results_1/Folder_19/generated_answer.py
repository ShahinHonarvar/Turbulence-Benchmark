
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(2, len(my_list), 2):
        if my_list[i] % 2 == 0:
            return my_list[i:]
    # If no even integers exist in the specified range, return an empty list
    return []
