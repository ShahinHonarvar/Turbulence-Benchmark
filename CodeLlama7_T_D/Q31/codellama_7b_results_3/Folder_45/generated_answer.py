
def if_perfect_num(my_list):
    # Check if the list is empty or if it has less than 34 elements
    if len(my_list) == 0 or len(my_list) < 34:
        return False

    # Get the integer at index 33
    num = my_list[33]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i
            if sum == num:
                return True

    return False
