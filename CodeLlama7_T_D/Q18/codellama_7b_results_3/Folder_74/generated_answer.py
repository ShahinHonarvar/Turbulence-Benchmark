
def sum_ints_div_by_either_nums(my_list):
    # Initialize the sum variable
    sum = 0

    # Loop through the list from index 90 to 97, both inclusive
    for i in range(90, 98):
        # Check if the current element is divisible by either 13 or 35
        if my_list[i] % 13 == 0 or my_list[i] % 35 == 0:
            # If it is, add it to the sum
            sum += my_list[i]

    # Return the sum of all integers divisible by either 13 or 35 from index 90 to index 97, both inclusive. If no such integers exist in the specified range, the function should return 0.
    return sum
