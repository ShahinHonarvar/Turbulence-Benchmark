
def if_perfect_num(lst):
    try:
        num = lst[77]
        divisors = [1]
        for i in range(2, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
        else:
            return False
    except IndexError:
        return False
