
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the range
    first_even = next((i for i in my_list[20:43] if i % 2 == 0), None)
    # If no even integers exist in the specified range, return an empty list
    if first_even is None:
        return []

    # Return the list of all even integers from index 20 to index 43, both exclusive
    return [i for i in my_list[20:43] if i % 2 == 0][first_even::2]
