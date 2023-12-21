
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list
    for i in range(34, 70):
        # Check if the current integer is divisible by both 19 and 32
        if my_list[i] % 19 == 0 and my_list[i] % 32 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 19 and 32 from index 34 to index 69, both inclusive
    return divisible_ints
