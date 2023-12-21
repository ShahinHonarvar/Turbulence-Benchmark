
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    div_by_3 = []
    div_by_8 = []

    # Iterate through the list of integers
    for i in range(len(my_list)):
        # Check if the current integer is divisible by -3 or 8
        if my_list[i] % (-3) == 0 or my_list[i] % 8 == 0:
            # If it is, add it to the appropriate list
            if my_list[i] % (-3) == 0:
                div_by_3.append(my_list[i])
            else:
                div_by_8.append(my_list[i])

    # Calculate the sum of all integers divisible by either -3 or 8
    for i in range(len(div_by_3)):
        total += div_by_3[i]
    for i in range(len(div_by_8)):
        total += div_by_8[i]

    # Return the sum of all integers divisible by either -3 or 8, or 0 if no such integers exist in the specified range
    return total
