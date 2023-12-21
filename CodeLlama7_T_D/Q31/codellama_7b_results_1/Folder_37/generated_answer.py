
def if_perfect_num(my_list):
    # Check if the list has at least 29 elements
    if len(my_list) < 29:
        return False

    # Get the value of the 28th element in the list
    num = my_list[28]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i
            if sum == num:
                return True

    return False
