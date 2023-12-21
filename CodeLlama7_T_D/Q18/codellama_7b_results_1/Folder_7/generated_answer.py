
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum to 0
    total = 0
    # Loop through the specified range of the list
    for i in range(543, 585 + 1):
        # Check if the current element is divisible by either -553 or -737
        if my_list[i] % (-553) == 0 or my_list[i] % (-737) == 0:
            # If it is, add it to the total
            total += my_list[i]
    # Return the sum of all integers divisible by either -553 or -737 from index 543 to index 584, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return total
