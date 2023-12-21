
def if_perfect_num(my_list):
    # Check if the index is out of range
    if len(my_list) - 1 < 222:
        return False

    # Find the sum of the factors of the number at index 222
    sum_of_factors = 0
    for i in range(1, my_list[222]):
        if my_list[222] % i == 0:
            sum_of_factors += i

    # Return True if the sum of factors is equal to the number at index 222, otherwise return False
    return sum_of_factors == my_list[222]
