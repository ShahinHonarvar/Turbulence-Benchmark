
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of the input list
    for i in range(200, len(my_list)):
        # Check if the current integer is divisible by both 17 and -5
        if my_list[i] % 17 == 0 and my_list[i] % -5 == 0:
            # If it is, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 17 and -5 from index 200 to index 200, both inclusive
    return divisible_ints
