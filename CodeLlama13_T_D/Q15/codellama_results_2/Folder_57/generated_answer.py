
def sum_odd_ints_inclusive(my_list):
    # Slice the list to include only odd integers from index 27 to index 55, both inclusive
    sliced_list = my_list[27:56:2]
    
    # Use sum() to calculate the sum of the sliced list
    return sum(sliced_list) if sliced_list else 0
