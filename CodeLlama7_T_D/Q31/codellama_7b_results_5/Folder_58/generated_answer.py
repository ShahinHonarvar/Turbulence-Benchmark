
def if_perfect_num(lst):
    index = 714
    if index < len(lst) and is_perfect_number(lst[index]):
        return True

    else:

        return False

def is_perfect_number(n):

    if n <= 0:

        return False


    sum = 1

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            sum += i + n // i


    return sum == n
