
def if_perfect_num(lst):
    def is_perfect(num):
        factor_sum = sum([i for i in range(1,num) if num % i == 0])
        return factor_sum == num    
    
    try:
        return is_perfect(lst[57])
    except IndexError:
        return False
