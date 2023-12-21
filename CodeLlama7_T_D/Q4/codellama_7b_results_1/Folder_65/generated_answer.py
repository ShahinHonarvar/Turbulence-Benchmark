
def all_pos_ints_exclusive(my_list):
    # Find the first positive integer in the list, starting from index 42
    start_index = next((i for i, x in enumerate(my_list) if x > 0), 42)
    # Find the last positive integer in the list, starting from index 87
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x > 0), len(my_list[start_index:])) + start_index
    return my_list[start_index:end_index]
