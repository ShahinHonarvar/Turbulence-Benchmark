
def all_ints_not_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Iterate over the list and check if each integer is not divisible by -68
    for i in range(29, 53):
        if my_list[i] % -68 != 0:
            # If the integer is not divisible by -68, add it to the results list
            results.append(my_list[i])

    # Return the results list

    return results
