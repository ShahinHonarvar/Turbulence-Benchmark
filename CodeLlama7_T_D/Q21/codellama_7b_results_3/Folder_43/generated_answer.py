
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the results
    results = []

    # Loop through the list and check if each element is divisible by -64
    for i in range(10, 37 + 1):
        if my_list[i] % -64 == 0:
            # If the element is divisible by -64, add it to the results list
            results.append(my_list[i])

    # Return the results list
    return results
