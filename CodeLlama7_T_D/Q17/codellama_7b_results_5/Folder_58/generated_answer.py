 def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of the input list
    for i in range(240, 901 + 1):

        # Check if the current element is divisible by both 546 and 709
        if my_list[i] % 546 == 0 and my_list[i] % 709 == 0:

            # If it is, append it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
