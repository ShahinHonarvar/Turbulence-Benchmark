
def if_perfect_num(lst):
    if lst[59] == sum(divisor for divisor in range(1, lst[59]) if lst[59] % divisor == 0):
        return True
    else:
        return False
