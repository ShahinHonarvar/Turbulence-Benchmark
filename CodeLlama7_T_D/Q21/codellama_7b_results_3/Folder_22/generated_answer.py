
def all_ints_div_by_num(my_list):
    # Create a new list to store the divisible integers
    divisible_integers = []
    # Iterate through the list of integers
    for i in range(10, len(my_list)):
        # Check if the current integer is divisible by 1
        if my_list[i] % 1 == 0:
            # If it is divisible, add it to the new list
            divisible_integers.append(my_list[i])
    return divisible_integers
