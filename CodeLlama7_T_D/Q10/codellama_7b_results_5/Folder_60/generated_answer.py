
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the range
    first_odd = next((i for i in my_list[44:91] if i % 2 == 1), None)
    # If no odd integers exist in the range, return an empty list
    if first_odd is None:
        return []

    # Find the last odd integer in the range

    last_odd = next(reversed(my_list[44:91]), None)

    # Return the list of all odd integers from index 44 to index 91, both exclusive
    return my_list[44:91][first_odd::last_odd]]
