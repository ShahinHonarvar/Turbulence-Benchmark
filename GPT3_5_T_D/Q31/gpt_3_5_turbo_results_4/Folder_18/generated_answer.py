
def if_perfect_num(lst):
    num = lst[312]
    factors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num//i)
    
    if sum(factors) == num:
        return True
    else:
        return False
