
def all_even_ints_exclusive(my_list):
    # Find the first even integer in the range
    start_index = next((i for i, x in enumerate(my_list) if x % 2 == 0), len(my_list))
    # Find the last even integer in the range
    end_index = next((i for i, x in enumerate(my_list[start_index:]) if x % 2 == 0), 0)
    # Return the list of all even integers in the range
    return my_list[start_index:end_index]
