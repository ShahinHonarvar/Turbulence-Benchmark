
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list and check if each element is divisible by -57
    for i in range(23, len(my_list)):
        if my_list[i] % -57 == 0:
            # If the element is divisible by -57, append it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
