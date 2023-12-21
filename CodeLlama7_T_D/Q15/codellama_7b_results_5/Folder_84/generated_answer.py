
def sum_odd_ints_inclusive(my_list):
    # Initialize the sum to 0
    sum = 0
    # Iterate over the list from index 43 to index 86, both inclusive
    for i in range(43, 87):
        # Check if the current element is an odd integer
        if my_list[i] % 2 != 0:
            # Add the current element to the sum
            sum += my_list[i]
    return sum
