
def all_odd_ints_inclusive(my_list):
    # Get the indices of the odd integers in the specified range
    start = 82
    end = 86
    odd_indices = [i for i, x in enumerate(my_list[start:end+1]) if x % 2 != 0]
    # Return the list of all odd integers from index 82 to index 86, both inclusive
    return [my_list[i] for i in odd_indices]
