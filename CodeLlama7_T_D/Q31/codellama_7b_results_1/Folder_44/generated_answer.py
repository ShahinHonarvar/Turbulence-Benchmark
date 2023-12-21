
def if_perfect_num(my_list):
    if len(my_list) > 828:
        num = my_list[828]
        sum = 0

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i

                if num / i != i:
                    sum += num / i

        if sum == num:
            return True

        else:
            return False

    else:
        return False
