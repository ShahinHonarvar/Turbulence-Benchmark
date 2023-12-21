
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    result = []

    # Iterate through the list and check if each element is not divisible by -77
    for i in range(len(my_list)):
        if my_list[i] % (-77) != 0:
            # If the element is not divisible by -77, add it to the result list
            result.append(my_list[i])

    # Return the result list
    return result
