
def all_ints_div_by_both_two_nums(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate over the list of integers and check if each integer is divisible by both 11 and -7. If it is, append it to the list of divisible integers
    for i in range(len(my_list)):
        if my_list[i] % 11 == 0 and my_list[i] % -7 == 0:
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by both 11 and -7 from index 0 to index 3, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
    return divisible_ints
