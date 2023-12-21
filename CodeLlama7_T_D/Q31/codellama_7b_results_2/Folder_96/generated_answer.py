
def if_perfect_num(my_list):
    # Check if the list has 48 elements
    if len(my_list) != 48:
        return False

    # Check if the number at index 47 is a perfect number
    if my_list[47] == 0:
        return False

    sum = 1

    for i in range(2, my_list[47]):
        if my_list[47] % i == 0:
            sum += i

    if sum == my_list[47]:
        return True

    else:

        return False
