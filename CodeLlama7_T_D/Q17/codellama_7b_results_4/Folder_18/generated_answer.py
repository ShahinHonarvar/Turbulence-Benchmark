
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list from index 55 to index 66, both inclusive
    for i in range(55, 67):
        # Check if the current integer is divisible by both 22 and 82
        if my_list[i] % 22 == 0 and my_list[i] % 82 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 22 and 82 from index 55 to index 66, both inclusive
    return divisible_ints
