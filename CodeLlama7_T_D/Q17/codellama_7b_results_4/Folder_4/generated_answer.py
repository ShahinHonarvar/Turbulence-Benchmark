 def all_ints_div_by_both_two_nums(my_list):
    # Initialize variables
    start_index = 86
    end_index = 90
    num1 = -71
    num2 = -67

    # Initialize an empty list to store the result
    result_list = []

    # Iterate through the specified range of the input list
    for i in range(start_index, end_index + 1):
        # Check if the current element is divisible by both num1 and num2
        if my_list[i] % num1 == 0 and my_list[i] % num2 == 0:
            # If it is, add it to the result list
            result_list.append(my_list[i])

    # Return the result list
    return result_list
