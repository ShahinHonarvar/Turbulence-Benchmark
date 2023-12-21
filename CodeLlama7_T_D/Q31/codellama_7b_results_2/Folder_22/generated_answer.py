
def if_perfect_num(my_list):
    # Check if the list has at least 73 elements
    if len(my_list) < 73:
        return False

    # Calculate the sum of the factors of the number at index 72
    perfect_sum = 0

    for i in range(1, my_list[72]):
        if my_list[72] % i == 0:
            perfect_sum += i

    # Check if the sum of the factors is equal to the number at index 72
    if perfect_sum == my_list[72]:
        return True

    else:

        return False
