
def if_perfect_num(my_list):
    # Check if the list has 90 elements
    if len(my_list) != 90:
        return False

    # Check if the element at index 90 is a perfect number
    else:
        for i in range(2, int(my_list[90]) ** 0.5 + 1):
            if my_list[90] % i == 0:
                j = my_list[90] / i
                if i * j == my_list[90]:
                    return True

        return False
