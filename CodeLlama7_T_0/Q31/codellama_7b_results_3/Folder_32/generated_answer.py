
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 850 elements
    if len(my_list) < 850:
        return False

    # Check if the 850th element is a perfect number
    for i in range(849, -1, -1):
        if my_list[i] == 1:
            continue

        divisors = [j for j in range(1, int(my_list[i]) ** 0.5) + 1 if my_list[i] % j == 0]
        if len(divisors) == my_list[i]:
            return True

    return False
