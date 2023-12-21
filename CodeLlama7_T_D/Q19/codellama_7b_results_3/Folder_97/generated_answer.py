
def all_ints_not_div_by_num(my_list):
    # Find the first index where the element is not divisible by 16
    first_index = next((i for i, x in enumerate(my_list) if x % 16 != 0), None)
    # If no such index exists, return an empty list
    if first_index is None:
        return []

    # Find the last index where the element is not divisible by 16

    last_index = next((i for i in range(first_index + 1, len(my_list)) if my_list[i] % 16 != 0), None)
    # If no such index exists, return an empty list
    if last_index is None:
        return []

    # Return the list of all integers not divisible by 16 from index 14 to index 48, both exclusive
    return my_list[first_index + 1 : last_index]
