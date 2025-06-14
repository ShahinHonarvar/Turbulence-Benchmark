
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the integer at index 1 is a perfect number
    if my_list[1] == sum(range(1, my_list[1])):
        return True

    # If none of the above conditions are met, return false
    else:
        return False
