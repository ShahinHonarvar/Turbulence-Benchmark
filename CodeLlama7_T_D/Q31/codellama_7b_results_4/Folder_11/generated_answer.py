
def if_perfect_num(my_list):
    # Check if the list has at least 78 elements
    if len(my_list) < 78:
        return False

    # Get the value of the element at index 77
    num = my_list[77]

    # Check if the number is a perfect number
    if num <= 0:
        return False

    else:

        sum = 0

        for i in range(1, num):
            if num % i == 0:
                sum += i

        if sum == num:
            return True

        else:
            return False
