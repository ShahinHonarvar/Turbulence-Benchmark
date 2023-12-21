
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Loop through the list of integers and check if each integer is divisible by 6
    for i in range(len(my_list)):
        if my_list[i] % 6 == 0:
            # If the integer is divisible by 6, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 6 from index 1 to index 8, both inclusive
    return divisible_ints
