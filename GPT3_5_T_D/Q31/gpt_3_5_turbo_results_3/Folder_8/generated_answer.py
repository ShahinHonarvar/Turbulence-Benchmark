
def if_perfect_num(lst):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        if sum(factors) == num:
            return True
        return False
    
    if len(lst) > 49:
        num = lst[49]
        return is_perfect(num)
    return False
