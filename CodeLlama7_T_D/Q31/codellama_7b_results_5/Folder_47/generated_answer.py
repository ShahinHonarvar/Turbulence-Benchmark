
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the integer at index 34 is a perfect number
    if my_list[34] in range(1, 10**6):
        sum = 0
        for i in range(1, my_list[34]):
            if my_list[34] % i == 0:
                sum += i

        return sum == my_list[34]

    else:

        return False
