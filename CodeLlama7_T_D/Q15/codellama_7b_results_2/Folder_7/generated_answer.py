
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through list from index 661 to index 924
    for i in range(661, 925):
        # If the current element is an odd integer, add it to sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return sum
    return sum
