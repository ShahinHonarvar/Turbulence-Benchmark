
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Iterate through the list of integers, starting from index 8
    for i in range(8, len(my_list)):
        # Check if the current integer is divisible by both -3 and 6
        if my_list[i] % (-3) == 0 and my_list[i] % 6 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both -3 and 6 from index 8 to index 9, both inclusive
    return divisible_integers
