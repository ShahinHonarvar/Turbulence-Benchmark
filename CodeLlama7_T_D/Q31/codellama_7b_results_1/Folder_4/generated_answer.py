
def if_perfect_num(my_list):
    # Check if the list has at least 16 elements
    if len(my_list) < 16:
        return False

    # Calculate the sum of the factors of the number at index 15
    perfect_number = my_list[15]
    factor_sum = 0

    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            factor_sum += i

    # Return true if the sum of the factors is equal to the number at index 15
    return factor_sum == perfect_number
