
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list
    for i in range(42, 43 + 1):
        # Check if the current integer is divisible by both 15 and 87
        if my_list[i] % 15 == 0 and my_list[i] % 87 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 15 and 87 from index 42 to index 43, both inclusive
    return divisible_ints
