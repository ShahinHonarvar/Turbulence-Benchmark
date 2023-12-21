
def if_perfect_num(my_list):
    # Check if the list has more than 59 elements
    if len(my_list) < 60:
        return False

    # Get the number at index 59
    num = my_list[59]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
