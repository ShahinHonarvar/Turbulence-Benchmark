
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 43 elements
    if len(my_list) < 43:
        return False

    # Check if the integer at index 43 is a perfect number
    if my_list[42] == 0:
        return False

    perfect_number = my_list[42]

    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            sum += i

    if sum == perfect_number:
        return True

    else:
        return False
