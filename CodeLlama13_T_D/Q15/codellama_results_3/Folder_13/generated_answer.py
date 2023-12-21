
def sum_odd_ints_inclusive(my_list):
    # Slice the list from index 25 to index 87, both inclusive
    sliced_list = my_list[25:88]

    # Filter out all even integers
    filtered_list = [x for x in sliced_list if x % 2 != 0]

    # Sum up the remaining odd integers
    return sum(filtered_list)
