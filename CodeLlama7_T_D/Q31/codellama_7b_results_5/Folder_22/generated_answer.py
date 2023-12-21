
def if_perfect_num(my_list):
    # Check if the list has 72 elements
    if len(my_list) != 72:
        return False

    # Get the integer at index 72
    num = my_list[72]

    # Check if the integer is a perfect number
    if num == 0 or num % 2 != 0:
        return False

    sum = 0

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == num
