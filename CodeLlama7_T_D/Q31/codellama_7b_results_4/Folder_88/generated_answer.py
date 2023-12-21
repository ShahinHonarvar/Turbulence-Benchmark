
def if_perfect_num(my_list):
    # Check if the list has enough elements
    if len(my_list) < 46:
        return False

    # Check if the integer at index 46 is a perfect number
    num = my_list[46]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    return sum == num
