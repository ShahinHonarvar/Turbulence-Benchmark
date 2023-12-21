
def if_perfect_num(lst):
    if len(lst) < 733:
        return False

    num = lst[733]

    if num <= 0:

        return False


    sqrt_num = int(round(math.sqrt(num), 0)))

    sum_of_factors = 0

    for i in range(1, sqrt_num + 1):

        if num % i == 0:

            sum_of_factors += i + (num // i)

    return sum_of_factors == num
