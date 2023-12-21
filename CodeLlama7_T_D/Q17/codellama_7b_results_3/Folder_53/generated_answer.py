
def all_ints_div_by_both_two_nums(my_list):
    # Define the range of indices to check
    start_index = 200
    end_index = 200
    # Initialize an empty list to store the results
    result_list = []
    # Loop through the range of indices and check if each integer is divisible by both 17 and -5
    for i in range(start_index, end_index + 1):
        if my_list[i] % 17 == 0 and my_list[i] % -5 == 0:
            # If the integer is divisible by both 17 and -5, append it to the result list
            result_list.append(my_list[i])
    return result_list
