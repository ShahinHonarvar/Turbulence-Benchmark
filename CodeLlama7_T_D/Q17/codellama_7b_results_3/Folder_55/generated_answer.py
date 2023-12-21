
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    div_ints = []

    # Iterate over the list of integers and check if each integer is divisible by both 10 and 100
    for i in range(len(my_list)):
        if my_list[i] % 10 == 0 and my_list[i] % 100 == 0:
            # If the integer is divisible by both 10 and 100, add it to the list of divisible integers
            div_ints.append(my_list[i])

    # Return the list of all integers divisible by both 10 and 100 from index 0 to index 9, both inclusive
    return div_ints
