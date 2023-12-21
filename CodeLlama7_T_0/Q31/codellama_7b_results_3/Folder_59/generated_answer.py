
def if_perfect_num(my_list):
    # Check if the list has at least three elements
    if len(my_list) < 3:
        return False

    # Get the third element of the list
    num = my_list[2]

    # Check if the number is a perfect number
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
