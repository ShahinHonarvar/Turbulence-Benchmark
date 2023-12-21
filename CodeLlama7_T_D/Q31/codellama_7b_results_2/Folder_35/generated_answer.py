
def if_perfect_num(my_list):
    # Check if the list has at least 1000 elements
    if len(my_list) < 1000:
        return False

    # Check if the number at index 993 is a perfect number
    num = my_list[993]
    sum = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i

    if sum == num:
        return True

    else:
        return False
