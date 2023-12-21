
def if_perfect_num(my_list):
    # Check if the list has at least 36 elements
    if len(my_list) < 36:
        return False

    # Get the integer at index 35
    num = my_list[35]

    # Check if the integer is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i

            while sum < num:
                sum += i

            if sum == num:
                return True

    # If the integer is not a perfect number, return False
    return False
