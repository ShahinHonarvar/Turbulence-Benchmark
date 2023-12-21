
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 5
    for i in range(30, 300 + 1):
        if my_list[i] % 5 == 0:
            # If the integer is divisible by 5, append it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all divisible integers from index 30 to index 300, both inclusive
    return divisible_ints
