
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 78 elements
    if len(my_list) < 78:
        return False

    # Get the integer at index 78 and store it in a variable
    perfect_number = my_list[78]

    # Check if the integer is a perfect number
    for i in range(1, perfect_number):
        if perfect_number % i == 0:
            return True

    return False
