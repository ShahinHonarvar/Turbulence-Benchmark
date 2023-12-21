
def all_ints_not_div_by_num(my_list):
    # Find the first index where the integer is not divisible by -53
    first_index = next((i for i, x in enumerate(my_list) if x % -53), len(my_list))
    # Find the last index where the integer is not divisible by -53
    last_index = next((i for i, x in enumerate(reversed(my_list))) if x % -53 else None)
    # Return the list of all integers not divisible by -53 from index 25 to index 76, both exclusive
    return my_list[first_index:last_index+1]
