
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 86 elements
    if len(my_list) < 86:
        return False

    # Calculate the sum of the factors of the number at index 85
    factor_sum = 0
    for i in range(1, my_list[85]):
        if my_list[85] % i == 0:
            factor_sum += i

    # Check if the sum of the factors is equal to the number at index 85
    if factor_sum == my_list[85]:
        return True

    else:

        return False
