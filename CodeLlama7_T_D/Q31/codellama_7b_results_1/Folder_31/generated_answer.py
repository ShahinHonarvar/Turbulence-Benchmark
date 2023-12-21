
def if_perfect_num(my_list):
    if my_list[66] == 0:
        return False

    else:

        for i in range(1, my_list[66]):
            if my_list[66] % i == 0:
                sum = 0

                for j in range(1, i + 1):
                    sum += j

                if sum == my_list[66]:
                    return True

        return False
