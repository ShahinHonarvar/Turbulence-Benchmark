
def all_odd_ints_exclusive(my_list):
    # Find the first odd integer in the list
    first_odd = next((i for i in my_list if i % 2 == 1), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd is None:
        return []

    # Find the last odd integer in the list

    last_odd = next((i for i in my_list[::-1] if i % 2 == 1), None)

    # Return the list of all odd integers from index 369 to index 983, both exclusive

    return [i for i in my_list[369:last_odd + 1] if i % 2 == 1]
