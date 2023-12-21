
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    num1 = -33
    num2 = -62

    # Loop through the list starting from index 81
    for i in range(81, len(my_list)):
        # Check if the current element is divisible by either num1 or num2
        if my_list[i] % num1 == 0 or my_list[i] % num2 == 0:
            # Add the current element to the total sum
            total += my_list[i]

    # Return the total sum
    return total
