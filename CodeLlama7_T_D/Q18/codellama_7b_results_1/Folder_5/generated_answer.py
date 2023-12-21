
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    div_by_6 = False
    div_by_4 = False

    # Iterate through the list
    for i in range(len(my_list)):
        # Check if the current integer is divisible by either -6 or 4
        if my_list[i] % (-6) == 0 or my_list[i] % 4 == 0:
            # If it is, set the corresponding flag to True
            if my_list[i] % (-6) == 0:
                div_by_6 = True

            else:

                div_by_4 = True

            # Add the current integer to the total
            total += my_list[i]

    # If neither flag is set, return 0
    if not div_by_6 and not div_by_4:
        return 0

    # Otherwise, return the sum of all integers divisible by either -6 or 4 from index 0 to index 1, both inclusive
    else:

        return total
