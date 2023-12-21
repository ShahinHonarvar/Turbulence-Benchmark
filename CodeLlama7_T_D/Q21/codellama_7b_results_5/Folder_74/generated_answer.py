
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 99
    for i in range(len(my_list)):
        if my_list[i] % 99 == 0:
            # If the integer is divisible by 99, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers from index 62 to index 63, both inclusive
    return divisible_ints
