
def if_perfect_num(my_list):
    if my_list[83] == 0:
        return False

    else:

        sum = 0

        for i in range(1, my_list[83]):
            if my_list[83] % i == 0:
                sum += i

        if sum == my_list[83]:
            return True

        else:

            return False
