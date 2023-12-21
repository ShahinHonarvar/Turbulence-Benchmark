
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list and check if each integer is divisible by 22
    for i in range(43, 60):
        if my_list[i] % 22 == 0:
            # If the integer is divisible by 22, add it to the result list
            result.append(my_list[i])

    # Return the result list

    return result
