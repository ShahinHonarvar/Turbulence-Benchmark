
def if_perfect_num(lst):
    def is_perfect(num):
        factors = []
        for i in range(1, num//2+1):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    if len(lst) >= 49:
        return is_perfect(lst[48])
    else:
        return False
