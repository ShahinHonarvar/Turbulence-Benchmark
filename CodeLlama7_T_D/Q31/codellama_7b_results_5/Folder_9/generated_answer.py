
def if_perfect_num(my_list):
    # Check if the list has at least 25 elements
    if len(my_list) < 25:
        return False

    # Check if the element at index 24 is a perfect number
    else:
        num = my_list[24]
        sum = 0

        for i in range(1, num):
            if num % i == 0:
                sum += i

        return sum == num
