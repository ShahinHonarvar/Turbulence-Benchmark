
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 86 elements
    if len(my_list) < 86:
        return False

    # Get the value of the element at index 85
    num = my_list[85]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num and (i - 1) * (j - 1) == num:
                return True

    # If the number is not a perfect number, return false
    return False
