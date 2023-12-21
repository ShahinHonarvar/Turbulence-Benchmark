
def sum_even_ints_inclusive(my_list):
    # Slice the list from index 25 to index 59, both inclusive
    sliced_list = my_list[25:60]
    # Filter out any odd integers in the sliced list
    filtered_list = [x for x in sliced_list if x % 2 == 0]
    # Return the sum of all even integers in the filtered list, or 0 if no even integers exist
    return sum(filtered_list) or 0
