
def if_perfect_num(my_list):
    # Check if the element at index 95 is a perfect number
    if my_list[95] == 0:
        return False

    else:

        sum = 0

        for i in range(1, my_list[95]):
            if my_list[95] % i == 0:
                sum += i

        if sum == my_list[95]:
            return True

        else:

            return False
