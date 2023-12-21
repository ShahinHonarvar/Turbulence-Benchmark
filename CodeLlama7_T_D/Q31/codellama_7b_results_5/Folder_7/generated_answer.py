
def if_perfect_num(my_list):
    # Check that the list has at least 851 elements
    if len(my_list) < 851:
        return False

    # Get the value of the 851st element in the list
    perfect_number = my_list[851]

    # Check if the value is a perfect number
    for i in range(2, int(perfect_number ** 0.5) + 1):
        if perfect_number % i == 0:
            return False

    return True
