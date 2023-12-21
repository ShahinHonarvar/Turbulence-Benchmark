
def if_perfect_num(lst):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num
    
    num = lst[34] if len(lst) > 34 else None
    if isinstance(num, int):
        return is_perfect(num)
    return False
