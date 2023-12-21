 `def gcf_two_nums(my_list):
    return gcf(my_list[28], my_list[20])
def gcf(a, b):
    if a == 0:
        return b

    while True:

        if a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2

        elif a % 2 == 1 and b % 2 == 1:
            a //= 2
            b //= 2

        else:

            break

    return a`
