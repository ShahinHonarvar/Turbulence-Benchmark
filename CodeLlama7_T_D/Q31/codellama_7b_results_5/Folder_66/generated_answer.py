
def if_perfect_num(my_list):
    # Check if the list has at least 43 elements
    if len(my_list) < 43:
        return False

    # Find the sum of all factors of the number at index 42
    factor_sum = 0
    for i in range(1, my_list[42] // 2 + 1):
        if my_list[42] % i == 0:
            factor_sum += i

    # Return True if the sum of factors is equal to the number at index 42, otherwise return False
    return factor_sum == my_list[42]
