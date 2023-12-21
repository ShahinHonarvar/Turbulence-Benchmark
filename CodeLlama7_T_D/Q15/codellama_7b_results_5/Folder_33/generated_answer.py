
def sum_odd_ints_inclusive(my_list):
    # Initialize variables
    total = 0
    start_index = 667
    end_index = 774
    # Iterate over the list and add up the odd integers in the specified range
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            total += my_list[i]
    return total
