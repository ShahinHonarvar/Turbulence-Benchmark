
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers starting from index 3 to index 9, both inclusive
    for i in range(3, 10):
        # Check if the current integer is divisible by both 6 and 1
        if my_list[i] % 6 == 0 and my_list[i] % 1 == 0:
            # If so, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 6 and 1 from index 3 to index 9, both inclusive
    return divisible_ints
