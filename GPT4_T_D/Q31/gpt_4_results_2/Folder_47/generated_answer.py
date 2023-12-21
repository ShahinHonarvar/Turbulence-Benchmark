
def if_perfect_num(lst):
    num = lst[34]
    factors = [i for i in range(1,num) if num%i == 0]
    return True if sum(factors) == num else False
