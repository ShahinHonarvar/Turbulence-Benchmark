
def all_ints_div_by_both_two_nums(my_list):
    # Find the first index where both numbers are divisible
    start_index = next((i for i, x in enumerate(my_list) if x % 5 == 0 and x % 7 == 0), None)
    # If no such index exists, return an empty list
    if start_index is None:
        return []

    # Find the last index where both numbers are divisible
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 5 == 0 and x % 7 == 0), None)
    # If no such index exists, return an empty list
    if end_index is None:
        return []

    # Return the sublist of the input list that consists of all integers divisible by both 5 and 7 from start_index to end_index, inclusive
    return my_list[start_index:end_index+1]
