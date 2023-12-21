
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result_list = []
    # Iterate through the list of integers, starting from index 4 (inclusive) and ending at index 7 (exclusive)
    for i in range(4, len(my_list)):
        # Check if the current integer is not divisible by -6
        if my_list[i] % -6 != 0:
            # If the current integer is not divisible by -6, add it to the result list
            result_list.append(my_list[i])
    # Return the result list
    return result_list
