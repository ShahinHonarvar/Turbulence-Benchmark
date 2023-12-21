
def if_perfect_num(my_list):
    # Check if the list has exactly one element
    if len(my_list) != 1:
        return False

    # Get the integer at index 0
    num = my_list[0]

    # Check if the integer is a perfect number
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i

    return sum == num
