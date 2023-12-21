
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the integer at index 37 is a perfect number
    if my_list[37] == calculate_perfect_number(my_list[37])):
        return True
    else:
        return False
