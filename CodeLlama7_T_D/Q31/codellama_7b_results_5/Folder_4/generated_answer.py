
def if_perfect_num(my_list):
    # Check that the list has at least 16 elements
    if len(my_list) < 16:
        return False

    # Get the number at index 15
    perfect_number = my_list[15]

    # Check if the number is a perfect number
    for i in range(1, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            j = perfect_number / i

            # If i and j are equal, the number is a perfect number
            if i == j:
                return True

    # If we reach this point, the number is not a perfect number
    return False
