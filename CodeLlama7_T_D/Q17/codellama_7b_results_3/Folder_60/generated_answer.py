
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Iterate through the list of integers, starting from index 10 and ending at index 79 (inclusive)
    for i in range(10, 80):
        # Check if the current integer is divisible by both -74 and -58
        if my_list[i] % (-74 * -58) == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    # Return the list of all integers divisible by both -74 and -58 from index 10 to index 79 (inclusive)
    return divisible_integers
