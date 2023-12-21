
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    sum = 0
    start_index = 70
    end_index = 200
    # Iterate through the list from start to end index
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by either 3 or -300
        if my_list[i] % 3 == 0 or my_list[i] % -300 == 0:
            # If it is, add it to the sum
            sum += my_list[i]
    # Return the sum
    return sum
