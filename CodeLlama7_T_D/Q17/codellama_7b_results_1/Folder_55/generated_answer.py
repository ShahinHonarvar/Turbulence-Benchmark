
def all_ints_div_by_both_two_nums(my_list):
    # Create a new list to store the divisible integers
    divisible_ints = []

    # Loop through the specified range of integers

    for i in range(0, 10):
        # Check if the current integer is divisible by both 10 and 100
        if my_list[i] % 10 == 0 and my_list[i] % 100 == 0:
            # If it is divisible, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    return divisible_ints
