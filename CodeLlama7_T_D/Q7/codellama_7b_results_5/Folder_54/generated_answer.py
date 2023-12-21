
def all_even_ints_inclusive(my_list):
    # Find the first even integer in the list
    first_even = next((i for i in my_list if i % 2 == 0), None)
    # If there are no even integers in the list, return an empty list
    if first_even is None:
        return []

    # Find the last even integer in the list

    last_even = next((i for i in my_list[::-1] if i % 2 == 0), None)

    # If there are no even integers in the range [34, 55], return an empty list

    if last_even is None:
        return []

    # Return a list of all even integers from index 34 to index 55, both inclusive

    return [i for i in my_list[34:56] if i % 2 == 0]
