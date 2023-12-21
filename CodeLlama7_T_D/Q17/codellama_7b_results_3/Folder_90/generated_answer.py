
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Iterate through the list of integers from index 138 to index 424, both inclusive
    for i in range(138, 425):
        # Check if the current integer is divisible by both -863 and -329
        if my_list[i] % -863 == 0 and my_list[i] % -329 == 0:
            # If it is, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    return divisible_integers
