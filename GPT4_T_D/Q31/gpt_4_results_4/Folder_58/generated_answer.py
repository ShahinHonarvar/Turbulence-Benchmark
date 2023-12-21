
def if_perfect_num(lst):
    try:
        num = lst[714]
        divisors = [x for x in range(1, num) if num % x == 0]
        return sum(divisors) == num
    except IndexError:
        return False
