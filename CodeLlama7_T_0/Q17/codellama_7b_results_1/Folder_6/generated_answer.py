
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of indices in the input list
    for i in range(41, 57):
        # Check if the current integer is divisible by both 82 and 90
        if my_list[i] % 82 == 0 and my_list[i] % 90 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 82 and 90 from index 41 to index 56, both inclusive
    return divisible_ints
