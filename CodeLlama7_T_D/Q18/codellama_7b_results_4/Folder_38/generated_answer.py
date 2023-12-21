
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables to keep track of the sum and the index
    sum = 0
    index = 10
    # Iterate through the list, starting from index 10
    for i in range(index, len(my_list)):
        # Check if the current element is divisible by either -40 or -12
        if my_list[i] % -40 == 0 or my_list[i] % -12 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
