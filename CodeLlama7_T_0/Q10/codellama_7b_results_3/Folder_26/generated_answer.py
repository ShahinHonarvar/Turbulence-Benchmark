
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    first_odd = next((i for i in my_list[44:78] if i % 2 != 0), None)
    # If no odd integers exist in the range, return an empty list
    if first_odd is None:
        return []

    # Return the list of all odd integers from index 44 to index 78, both exclusive
    return [i for i in my_list[44:78] if i % 2 != 0]
