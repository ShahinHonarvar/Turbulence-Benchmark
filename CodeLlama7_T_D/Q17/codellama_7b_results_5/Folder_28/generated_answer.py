
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the specified range of the input list
    for i in range(34, 82):
        # Check if the current element is divisible by both 27 and 57
        if my_list[i] % 27 == 0 and my_list[i] % 57 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
