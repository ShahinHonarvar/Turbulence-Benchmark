
def if_perfect_num(my_list):
    # Check if the list has 100 elements
    if len(my_list) != 100:
        return False

    # Get the value of the 100th element
    perfect_number = my_list[99]

    # Check if the number is perfect by dividing it by all numbers less than itself and checking if the result is equal to itself.
    for i in range(1, perfect_number):
        if perfect_number % i != 0:
            return False

    # If the number is perfect, return true
    return True
