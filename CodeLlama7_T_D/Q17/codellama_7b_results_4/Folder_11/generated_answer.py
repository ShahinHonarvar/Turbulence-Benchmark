
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the list of integers, starting from index 22 and ending at index 24 (both inclusive)
    for i in range(22, 25):
        # Check if the current integer is divisible by both -85 and -30
        if my_list[i] % (-85) == 0 and my_list[i] % (-30) == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both -85 and -30 from index 22 to index 24, both inclusive
    return divisible_integers
