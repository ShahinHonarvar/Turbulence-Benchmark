
def all_pos_ints_inclusive(my_list):
    # Find the first positive integer in the list
    first_positive = next((i for i in my_list if i > 0), None)
    # If no positive integers exist in the list, return an empty list
    if first_positive is None:
        return []

    # Find the last positive integer in the list

    last_positive = next(reversed(my_list), None)

    # Return the list of all positive integers from index 91 to index 99, both inclusive

    return [i for i in my_list[first_positive - 1:last_positive + 1] if i > 0]
