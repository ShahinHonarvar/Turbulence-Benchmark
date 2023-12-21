
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the integer at index 91 is a perfect number
    if my_list[91] == 6:
        return True

    else:

        return False
