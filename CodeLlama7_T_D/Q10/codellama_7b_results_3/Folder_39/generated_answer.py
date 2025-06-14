
def all_odd_ints_exclusive(my_list):
    # Check if there are any odd integers in the specified range
    if not any(i % 2 for i in my_list[43:99]):
        return []
    else:

        # Return the list of all odd integers from index 43 to index 99, both exclusive
        return [i for i in my_list[43:99] if i % 2]
