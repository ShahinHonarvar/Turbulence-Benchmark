
def all_odd_ints_inclusive(my_list):
    # Find the first odd integer in the range
    first_odd = next((i for i in my_list[56:98] if i % 2 == 1), None)
    # If no odd integers exist in the range, return an empty list
    if first_odd is None:
        return []

    # Return a list of all odd integers from index 56 to index 98, both inclusive
    return [i for i in my_list[56:98] if i % 2 == 1]
