
def if_perfect_num(lst):
    if len(lst) <= 410:
        return False

    num = lst[410]

    sum = 0

    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:

            sum += i


    if sum == num:

        return True


    else:

        return False
