
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the element at index 453 is a perfect number
    if my_list[453] in range(1, 10**7 + 1):
        sum = 0
        for i in range(1, my_list[453] + 1):
            if my_list[453] % i == 0:
                sum += i

        if sum == my_list[453]:
            return True

    return False
