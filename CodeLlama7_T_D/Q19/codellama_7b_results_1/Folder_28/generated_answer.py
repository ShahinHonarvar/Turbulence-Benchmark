
def all_ints_not_div_by_num(my_list):
    # Find the first index where the number is not divisible by 77
    first_index = next((i for i, x in enumerate(my_list) if x % 77 != 0), None)
    # If no such indices exist, return an empty list
    if first_index is None:
        return []

    # Find the last index where the number is not divisible by 77
    last_index = next((i for i, x in enumerate(my_list) if x % 77 != 0), None)
    # If no such indices exist, return an empty list
    if last_index is None:
        return []

    # Return the list of all integers not divisible by 77 from index 81 to index 86, both exclusive
    return my_list[first_index:last_index+1]
