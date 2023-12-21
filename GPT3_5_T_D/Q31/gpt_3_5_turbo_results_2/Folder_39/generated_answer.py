
def if_perfect_num(lst):
    def is_perfect(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        if sum(divisors) == n:
            return True
        return False

    if len(lst) > 59 and is_perfect(lst[59]):
        return True
    return False
