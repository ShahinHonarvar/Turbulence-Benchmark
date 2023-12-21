
def if_perfect_num(lst):
    if lst[132] < 1:
        return False
    sum = 0
    for i in range(1, lst[132]):
        if lst[132] % i == 0:
            sum += i
    return sum == lst[132]
