
def if_perfect_num(my_list):
    # Check if the list has at least 163 elements
    if len(my_list) < 163:
        return False

    # Get the value of the 162nd element in the list
    num = my_list[162]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num / i
            if i * j == num:
                return True

    return False
