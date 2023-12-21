
def if_perfect_num(lst):
    try:
        num = lst[702]
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num
    except IndexError:
        return False
