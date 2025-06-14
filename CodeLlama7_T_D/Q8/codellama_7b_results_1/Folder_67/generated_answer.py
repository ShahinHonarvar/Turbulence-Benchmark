
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the list
    for i in range(49, len(my_list)):
        if my_list[i] % 2 == 0:
            # If an even integer is found, return a new list with all even integers from index 49 to index 74, both exclusive
            return [my_list[j] for j in range(i+1, min(len(my_list), i+26)))]
    # If no even integers are found in the specified range, return an empty list
    return []
