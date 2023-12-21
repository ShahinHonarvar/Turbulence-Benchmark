
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_integers = []

    # Loop through the specified range of integers

    for i in range(10):

        # Check if the current integer is divisible by both 10 and 100

        if my_list[i] % 10 == 0 and my_list[i] % 100 == 0:

            # If it is, add it to the list of divisible integers

            divisible_integers.append(my_list[i])

    # Return the list of all integers divisible by both 10 and 100 from index 0 to index 9, both inclusive

    return divisible_integers
