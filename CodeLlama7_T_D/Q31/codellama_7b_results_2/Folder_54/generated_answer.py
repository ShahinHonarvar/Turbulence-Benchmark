
def if_perfect_num(my_list):
    # Check if the list has at least 51 elements
    if len(my_list) < 51:
        return False

    # Get the element at index 51
    num = my_list[51]

    # Check if the number is perfect
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

    return sum == num
