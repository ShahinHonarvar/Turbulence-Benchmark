
def all_ints_not_div_by_num(my_list):
    # Find the index of the first element that is not divisible by 602
    start_index = next((i for i, x in enumerate(my_list) if x % 602 != 0), len(my_list))
    # Find the index of the last element that is not divisible by 602
    end_index = next((i for i, x in enumerate(reversed(my_list)) if x % 602 != 0), len(my_list) - 1)
    # Return the list of all integers not divisible by 602 from index 472 to index 827, both exclusive
    return my_list[start_index:end_index + 1]
