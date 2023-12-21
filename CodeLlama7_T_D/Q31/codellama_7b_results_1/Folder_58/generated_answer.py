
def if_perfect_num(my_list):
    # Check if the list has at least 714 elements
    if len(my_list) < 714:
        return False

    # Get the number at index 714
    num = my_list[714]

    # Check if the number is a perfect number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum = i + num / i
            if sum == num:
                return True

    return False
