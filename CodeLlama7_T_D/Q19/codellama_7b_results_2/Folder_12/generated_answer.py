
def all_ints_not_div_by_num(my_list):
    # Check if the input is a list of integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) for x in my_list))):
        raise ValueError("Input must be a list of integers")

    # Initialize an empty list to store the results
    result = []

    # Iterate over the input list and check if each integer is not divisible by -26
    for i in range(len(my_list)):
        if my_list[i] % (-26) != 0:
            result.append(my_list[i])

    # Return the list of all integers not divisible by -26 from index 59 to index 93, both exclusive
    return result
