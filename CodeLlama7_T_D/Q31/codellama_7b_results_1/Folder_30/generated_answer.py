
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Get the number at index 94
    num = my_list[94]

    # Check if the number is a perfect number
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisor_sum = i + num / i
                if divisor_sum == num:
                    return True

    # If the number is not a perfect number, return False
    return False
