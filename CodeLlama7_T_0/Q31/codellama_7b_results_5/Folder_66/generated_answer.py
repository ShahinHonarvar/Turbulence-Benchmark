
def if_perfect_num(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Check if the element at index 42 is a perfect number
    if my_list[42] in range(1, 10**6 + 1):
        sum = 0
        for i in range(1, my_list[42] + 1):
            if my_list[42] % i == 0:
                sum += i

        if sum == my_list[42]:
            return True

    return False
