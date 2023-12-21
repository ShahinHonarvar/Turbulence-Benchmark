
def sum_ints_div_by_either_nums(my_list):
    # Extract the slice of the list from index 50 to index 200, both inclusive
    sliced_list = my_list[50:201]
    
    # Sum up all integers divisible by -34 or 64 in the sliced list
    summed_ints = sum(i for i in sliced_list if i % (-34) == 0 or i % 64 == 0)
    
    return summed_ints
