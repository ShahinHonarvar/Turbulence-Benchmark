
def if_perfect_num(lst):
    if len(lst) < 312:
        return False

    else:

        num = lst[312]

        divisors = []

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)

        return sum(divisors) == num
