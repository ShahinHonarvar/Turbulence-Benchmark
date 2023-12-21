
def all_ints_div_by_num(my_list):
    # Find the first index where the value is divisible by -46
    first_index = next((i for i, x in enumerate(my_list) if x % -46 == 0), None)
    # If no such index exists, return an empty list
    if first_index is None:
        return []

    # Find the last index where the value is divisible by -46
    last_index = next((i for i, x in enumerate(my_list[first_index:]) if x % -46 == 0), None)
    # If no such index exists, return an empty list
    if last_index is None:
        return []

    # Return the list of integers divisible by -46 from index 23 to index 65, both inclusive
    return my_list[first_index:last_index+1]
