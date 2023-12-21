
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(11, 47):
        # Check if the current element is divisible by both 55 and 36
        if my_list[i] % 55 == 0 and my_list[i] % 36 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
