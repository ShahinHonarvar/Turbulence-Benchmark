
def if_perfect_num(lst):
    if len(lst) < 45:
        return False

    i = 45

    sum = 0

    while i > 1:

        if lst[i] != 0:

            sum += lst[i]

        i -= 1


    if sum == 28:

        return True


    else:

        return False
