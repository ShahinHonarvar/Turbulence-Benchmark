
def all_ints_not_div_by_num(my_list):
    # Find the first index where a non-divisible number is found
    first_index = next((i for i, x in enumerate(my_list) if x % 97), None)
    # If no such index exists, return an empty list
    if first_index is None:
        return []

    # Find the last index where a non-divisible number is found
    last_index = next((i for i, x in enumerate(my_list[first_index:]) if x % 97), None)
    # If no such index exists, return an empty list
    if last_index is None:
        return []

    # Return the list of all integers not divisible by 97 from index 19 to index 69, both exclusive
    return my_list[first_index + 19:last_index + 19]
