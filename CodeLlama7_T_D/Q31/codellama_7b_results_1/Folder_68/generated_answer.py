
def if_perfect_num(my_list):
    # Check if the list has at least four elements
    if len(my_list) < 4:
        return False

    # Get the integer at index 3
    num = my_list[3]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == 2 * num
