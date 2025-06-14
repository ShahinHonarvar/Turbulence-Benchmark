
def if_perfect_num(my_list):
    # Check if the list is empty or has less than 846 elements
    if len(my_list) < 846:
        return False

    # Check if the element at index 845 is a perfect number
    if my_list[845] == 0:
        return False

    sum = 0

    for i in range(1, my_list[845]):
        if my_list[845] % i == 0:
            sum += i

    if sum == my_list[845]:
        return True

    else:

        return False
