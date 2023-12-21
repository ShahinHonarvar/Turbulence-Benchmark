
def all_ints_div_by_both_two_nums(my_list):
    # Find the first index where the value is divisible by both -33 and -62
    first_index = next((i for i, x in enumerate(my_list) if x % (-33 * -62) == 0), None)
    # If no such indices exist, return an empty list
    if first_index is None:
        return []

    # Find the last index where the value is divisible by both -33 and -62
    last_index = next((i for i, x in enumerate(my_list) if x % (-33 * -62) == 0)), None)
    # If no such indices exist, return an empty list
    if last_index is None:
        return []

    # Return the sublist of all integers divisible by both -33 and -62 from index 81 to index 86, both inclusive
    return my_list[first_index:last_index+1]
