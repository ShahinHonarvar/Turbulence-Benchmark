
def if_perfect_num(my_list):
    # Check if the list has at least 100 elements
    if len(my_list) < 100:
        return False

    # Get the number at index 99
    num = my_list[99]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num / i

    return sum == num
