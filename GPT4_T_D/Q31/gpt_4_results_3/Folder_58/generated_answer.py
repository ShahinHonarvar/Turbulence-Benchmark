
def if_perfect_num(lst):
    num =  lst[714] if len(lst)>714 else None
    if num is not None:
        sum = 0
        for i in range(1, num): 
            if num % i == 0:
                sum += i
        if sum == num:
            return True
    return False
