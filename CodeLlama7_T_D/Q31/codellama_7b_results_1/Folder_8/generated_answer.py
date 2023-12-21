
def if_perfect_num(my_list):
    # Check that the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Return true if the integer at index 49 is a perfect number, otherwise return false
    return (my_list[49] == sum(range(1, my_list[49])))
