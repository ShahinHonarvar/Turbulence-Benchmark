
def all_odd_ints_exclusive(my_list):
    # Find the index of the first odd integer in the list
    first_odd_index = next((i for i, x in enumerate(my_list) if x % 2 == 1)), None)
    # If no odd integers exist in the list, return an empty list
    if first_odd_index is None:
        return []

    # Find the index of the last odd integer in the list
    last_odd_index = len(my_list) - 1
    for i in range(len(my_list) - 1, -1, -1):
        if my_list[i] % 2 == 1:
            last_odd_index = i
            break

    # Return the list of all odd integers from index 361 to index 643, both exclusive
    return my_list[first_odd_index + 1:last_odd_index]
