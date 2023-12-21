
def all_ints_not_div_by_num(my_list):
    # Find the first index where the number is not divisible by 67
    start_index = next((i for i, x in enumerate(my_list) if x % 67 != 0), len(my_list))
    # Find the last index where the number is not divisible by 67
    end_index = next((i for i, x in enumerate(reversed(my_list))) if x % 67 != 0 else None, len(my_list))
    # Return the list of integers not divisible by 67 from index 46 to index 91, both exclusive
    return my_list[start_index:end_index]
