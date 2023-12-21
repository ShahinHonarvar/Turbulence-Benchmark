
def all_even_ints_exclusive(my_list):
    # Find the first even index in the range
    first_even = next((i for i, x in enumerate(my_list) if x % 2 == 0), None)
    # If there are no even integers in the range, return an empty list
    if first_even is None:
        return []

    # Find the last even index in the range

    last_even = next((i for i, x in enumerate(my_list[first_even:]) if x % 2 == 0), None)

    # Return the list of all even integers in the range, exclusive of the end indices

    return my_list[first_even:last_even + first_even]
