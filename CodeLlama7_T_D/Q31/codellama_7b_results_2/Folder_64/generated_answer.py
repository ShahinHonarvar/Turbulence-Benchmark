
def if_perfect_num(my_list):
    # Check if the list is empty
    if not my_list:
        return False

    # Get the integer at index 1
    num = my_list[1]

    # Check if the number is a perfect number
    for i in range(1, num):
        if num % i == 0:
            sum = i + num / i
            if sum == num:
                return True

    return False
