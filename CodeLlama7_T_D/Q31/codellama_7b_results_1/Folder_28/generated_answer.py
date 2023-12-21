
def if_perfect_num(my_list):
    # Check if the list has at least 38 elements
    if len(my_list) < 38:
        return False

    # Get the integer at index 37
    perfect_number = my_list[37]

    # Check if the integer is a perfect number
    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            sum_of_factors = i + perfect_number // i

            # Check if the sum of the factors is equal to the perfect number
            if sum_of_factors == perfect_number:
                return True

    return False
