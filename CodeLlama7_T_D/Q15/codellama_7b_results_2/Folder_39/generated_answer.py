
def sum_odd_ints_inclusive(my_list):
    # Initialize sum to 0
    sum = 0
    # Iterate over list from index 20 to index 30 (both inclusive)
    for i in range(20, 31):
        # Check if current element is an odd integer
        if my_list[i] % 2 != 0:
            # If yes, add it to sum
            sum += my_list[i]
    # Return sum
    return sum
