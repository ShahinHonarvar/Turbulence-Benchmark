
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Loop through list from index 1 to index 8, both inclusive
    for i in range(1, 9):
        # If current element is an odd integer, add it to sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return sum
