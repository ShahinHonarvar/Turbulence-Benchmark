
def all_ints_div_by_both_two_nums(my_list):
    # Define the range of indices to check
    start_index = 7
    end_index = 9
    # Initialize an empty list to store the divisible integers
    divisible_integers = []
    # Iterate through the range of indices and check if each integer is divisible by both 2 and 3
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 == 0 and my_list[i] % 3 == 0:
            # If the integer is divisible by both 2 and 3, add it to the list of divisible integers
            divisible_integers.append(my_list[i])
    return divisible_integers
