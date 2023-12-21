
def if_perfect_num(my_list):
    # Check if the list has at least 57 elements
    if len(my_list) < 57:
        return False

    # Get the integer at index 56
    perfect_number = my_list[56]

    # Check if the integer is a perfect number
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            sum = i + perfect_number / i

            if sum == perfect_number:
                return True

    return False
