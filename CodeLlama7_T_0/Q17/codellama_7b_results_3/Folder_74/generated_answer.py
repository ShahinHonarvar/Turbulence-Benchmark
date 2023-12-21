
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the specified range of the input list
    for i in range(90, 98):
        # Check if the current integer is divisible by both 13 and 35
        if my_list[i] % 13 == 0 and my_list[i] % 35 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 13 and 35 from index 90 to index 97, both inclusive
    return divisible_ints
