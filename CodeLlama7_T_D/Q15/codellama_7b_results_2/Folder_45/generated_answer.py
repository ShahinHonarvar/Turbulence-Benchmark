
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list from index 30 to index 200
    for i in range(30, 201):
        # If the current element is an odd integer, add it to the sum
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    # Return the sum
    return sum
