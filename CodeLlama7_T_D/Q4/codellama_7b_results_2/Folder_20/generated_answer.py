
def all_pos_ints_exclusive(my_list):
    # Find the starting and ending indices of the positive integers in the list
    start_idx = next((i for i, x in enumerate(my_list) if x > 0), len(my_list))
    end_idx = next((i for i, x in enumerate(my_list[start_idx:]) if x > 0), len(my_list[start_idx:])) + start_idx
    # Return the list of positive integers from the starting to ending index, both exclusive
    return my_list[start_idx:end_idx]
