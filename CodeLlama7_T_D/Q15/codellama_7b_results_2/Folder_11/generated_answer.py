
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate through list from index 37 to 51, both inclusive
    for i in range(37, 52):
        # If current element is an odd integer, add it to sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return sum
    return sum
