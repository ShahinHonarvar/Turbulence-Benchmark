
def if_perfect_num(lst):
    num = lst[410]
    
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        if sum(factors) == num:
            return True
        return False
    
    return is_perfect(num)
