
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list, starting from index 15
    start_index = next((i for i, x in enumerate(my_list) if x > 0), 15)
    # Find the last positive integer in the list, starting from index 40
    end_index = next((i for i, x in enumerate(my_list) if x > 0), 40)
    return [x for x in my_list[start_index:end_index]]
