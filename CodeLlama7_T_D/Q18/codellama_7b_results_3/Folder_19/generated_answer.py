
def sum_ints_div_by_either_nums(my_list):
    # Initialize variables
    total = 0
    i = 1

    while i <= 4:

        # Check if current element is divisible by either 4 or -6
        if my_list[i] % 4 == 0 or my_list[i] % -6 == 0:
            # Add current element to total
            total += my_list[i]

        # Increment index variable
        i += 1

    return total
