
def all_ints_div_by_num(my_list):
    # Define the divisor and range of indices
    divisor = -158
    start = 572
    end = 806
    # Initialize an empty list to store the results
    result_list = []
    # Loop through the specified range of indices
    for i in range(start, end + 1):
        # Check if the current element is divisible by the divisor
        if my_list[i] % divisor == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
