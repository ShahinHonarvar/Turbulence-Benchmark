
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of indices in the input list
    for i in range(154, 798 + 1):
        # Check if the current element is divisible by both 275 and 580
        if my_list[i] % 275 == 0 and my_list[i] % 580 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 275 and 580 from index 154 to index 798, both inclusive
    return divisible_ints
