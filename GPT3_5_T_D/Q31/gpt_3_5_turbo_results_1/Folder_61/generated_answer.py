
def if_perfect_num(lst):
    def is_perfect(num):
        if num <= 0:
            return False
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    if len(lst) >= 9:
        return is_perfect(lst[8])
    else:
        return False
