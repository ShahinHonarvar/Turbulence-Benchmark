
def if_perfect_num(my_list):
    # Check if the list has at least 98 elements
    if len(my_list) < 98:
        return False

    # Check if the number at index 97 is a perfect number
    if my_list[97] == 0:
        return False

    sum = 0

    for i in range(1, my_list[97]):
        if my_list[97] % i == 0:
            sum += i

    if sum == my_list[97]:
        return True

    else:

        return False
