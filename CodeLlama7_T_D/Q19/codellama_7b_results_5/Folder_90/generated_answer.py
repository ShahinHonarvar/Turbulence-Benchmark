
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the result
    result = []

    # Iterate through the input list
    for i in range(len(my_list)):

        # Check if the current element is not divisible by -430
        if my_list[i] % -430 != 0:

            # If it is not divisible, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
