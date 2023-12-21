
def all_ints_div_by_both_two_nums(my_list):
    # Create a list of integers divisible by both -3 and 8
    divisible_integers = []
    # Iterate through the list of integers
    for i in my_list:
        # Check if the current integer is divisible by both -3 and 8
        if (i % -3 == 0) and (i % 8 == 0):
            # If it is, add it to the list of divisible integers
            divisible_integers.append(i)
    # Return the list of all integers divisible by both -3 and 8 from index 0 to index 8, both inclusive
    return divisible_integers
