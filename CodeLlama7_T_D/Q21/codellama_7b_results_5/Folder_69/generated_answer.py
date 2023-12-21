
def all_ints_div_by_num(my_list):
    # Find the first index of the range that is divisible by 14
    start_index = next((i for i, x in enumerate(my_list) if x % 14 == 0), None)
    # If no such integer exists, return an empty list
    if start_index is None:
        return []

    # Find the last index of the range that is divisible by 14

    end_index = next((i for i in range(start_index, len(my_list)) if my_list[i] % 14 == 0)), None)
    # If no such integer exists, return an empty list
    if end_index is None:
        return []

    # Return the list of all integers divisible by 14 from index 43 to index 76, both inclusive
    return my_list[start_index:end_index+1]
