
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers
    for i in range(1, len(my_list)):
        # Check if the current integer is divisible by both 4 and -6
        if my_list[i] % 4 == 0 and my_list[i] % (-6) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 4 and -6 from index 1 to index 4, both inclusive
    return divisible_ints
