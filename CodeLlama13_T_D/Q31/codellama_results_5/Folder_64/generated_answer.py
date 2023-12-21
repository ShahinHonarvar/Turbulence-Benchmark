
def if_perfect_num(lst):
    if len(lst) < 1:
        return False
    
    n = lst[0]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return True
    return False
