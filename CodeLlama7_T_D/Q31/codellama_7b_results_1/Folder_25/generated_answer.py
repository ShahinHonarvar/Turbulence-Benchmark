
def if_perfect_num(my_list):
    # Check if the input is a list of positive integers
    if not (isinstance(my_list, list) and all(isinstance(x, int) and x > 0 for x in my_list)):
        raise ValueError("Input must be a list of positive integers")
    # Check if the index 90 is out of range
    if len(my_list) < 90:
        raise ValueError("Index out of range")
    # Calculate the sum of the digits of the number at index 90
    num = my_list[90]
    sum_digits = sum([int(digit) for digit in str(num)])
    # Check if the sum of the digits is equal to the number itself
    if sum_digits == num:
        return True

    else:

        return False
