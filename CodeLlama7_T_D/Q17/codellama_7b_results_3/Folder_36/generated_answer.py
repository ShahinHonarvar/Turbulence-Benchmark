
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate over the specified range of indices in the input list
    for i in range(299, 382 + 1):
        # Check if the current element is divisible by both 858 and 952
        if my_list[i] % 858 == 0 and my_list[i] % 952 == 0:
            # If so, add it to the result list
            result.append(my_list[i])

    # Return the resulting list of integers divisible by both 858 and 952
    return result
