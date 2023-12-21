
def all_ints_div_by_both_two_nums(my_list):
    # Find the first index where the current element is divisible by both 275 and 580
    first_index = next((i for i, x in enumerate(my_list) if x % 275 == 0 and x % 580 == 0), None)
    # If no such index exists, return an empty list
    if first_index is None:
        return []

    # Return the list of all integers divisible by both 275 and 580 from the specified range
    return [x for x in my_list[first_index:] if x % 275 == 0 and x % 580 == 0]
