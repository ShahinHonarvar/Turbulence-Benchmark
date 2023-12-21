
def if_perfect_num(my_list):
    # Check if the list is empty or not
    if len(my_list) == 0:
        return False

    # Check if the element at index 47 exists in the list or not
    if my_list[47] in my_list:
        # If the element at index 47 is a perfect number, then it is a prime number
        if is_prime(my_list[47]):
            return True

    return False
