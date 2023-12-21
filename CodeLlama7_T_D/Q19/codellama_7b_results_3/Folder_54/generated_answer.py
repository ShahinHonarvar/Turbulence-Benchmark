
def all_ints_not_div_by_num(my_list):
    # Find the first index where the number is divisible by -32
    start_index = next((i for i, x in enumerate(my_list) if x % (-32) == 0)), None)
    # Find the last index where the number is not divisible by -32
    end_index = next((i for i, x in enumerate(my_list) if x % (-32) != 0)), None)
    # Return an empty list if no such integers exist in the specified range
    if start_index is None or end_index is None:
        return []

    # Return the list of all integers not divisible by -32 from index 19 to index 94, both exclusive
    return my_list[start_index + 19:end_index + 19]
