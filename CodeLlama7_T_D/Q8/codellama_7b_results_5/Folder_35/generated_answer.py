 def all_even_ints_exclusive(my_list):
    # Get the indices of the even integers in the specified range
    start = 10
    end = 79
    even_indices = [i for i, x in enumerate(my_list) if x % 2 == 0 and start <= i < end]
    # Return an empty list if no even integers exist in the specified range
    if not even_indices:
        return []

    # Return the list of all even integers from index 10 to index 79, both exclusive
    return [my_list[i] for i in even_indices]
