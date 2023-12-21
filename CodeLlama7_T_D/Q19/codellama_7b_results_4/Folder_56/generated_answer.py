
def all_ints_not_div_by_num(my_list):
    # Find the first index where the number is not divisible by -9
    first_index = next((i for i, x in enumerate(my_list) if x % -9 != 0), len(my_list))
    # Find the last index where the number is not divisible by -9
    last_index = next((i for i, x in enumerate(my_list[::-1]) if x % -9 != 0), len(my_list))
    # Return the list of all integers not divisible by -9 from index 7 to index 9, both exclusive
    return my_list[first_index:last_index]
