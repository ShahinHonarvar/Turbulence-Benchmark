
def all_ints_div_by_num(my_list, num):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the input list and check if each element is divisible by -27
    for i in range(len(my_list)):
        if my_list[i] % num == 0:
            # If the element is divisible by -27, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
