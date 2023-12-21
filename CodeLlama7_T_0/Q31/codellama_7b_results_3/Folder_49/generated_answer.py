
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 69 elements
    if len(my_list) < 69:
        return False

    # Get the integer at index 68
    perfect_number = my_list[68]

    # Check if the integer is a perfect number
    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            sum_of_factors = i + perfect_number // i

            if sum_of_factors == perfect_number:
                return True

    # If the integer is not a perfect number, return False
    return False
