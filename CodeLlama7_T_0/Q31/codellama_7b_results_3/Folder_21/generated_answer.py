
def if_perfect_num(my_list):
    # Check if the list has at least 410 elements
    if len(my_list) < 410:
        return False

    # Get the value of the element at index 410
    num = my_list[410]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
