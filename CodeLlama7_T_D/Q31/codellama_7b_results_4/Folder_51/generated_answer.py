
def if_perfect_num(my_list):
    # Check if the list has at least 65 elements
    if len(my_list) < 65:
        return False

    # Calculate the sum of the factors of 64
    factor_sum = 0
    for i in range(1, int(math.sqrt(64)) + 1)):
        if 64 % i == 0:
            factor_sum += i

    # Return True if the sum is equal to 64, otherwise return False
    return factor_sum == 64
