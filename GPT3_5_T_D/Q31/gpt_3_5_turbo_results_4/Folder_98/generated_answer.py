
def if_perfect_num(lst):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        if sum(divisors) == num:
            return True
        return False

    if len(lst) >= 5 and is_perfect(lst[4]):
        return True
    return False
