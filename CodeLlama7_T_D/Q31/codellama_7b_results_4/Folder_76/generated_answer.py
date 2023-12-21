
def if_perfect_num(my_list):
    # Check if the list is empty or has fewer than 537 elements
    if len(my_list) < 537:
        return False

    # Check if the integer at index 537 is a perfect number
    if my_list[537] == 0:
        return False

    else:

        for i in range(1, int(my_list[537]) ** 0.5 + 1):
            if my_list[537] % i == 0:
                sum = i + my_list[537] / i
                if sum == my_list[537]:
                    return True

        return False
