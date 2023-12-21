
def if_perfect_num(lst):
    def perfect_num(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n

    if len(lst) > 993 and perfect_num(lst[993]):
        return True
    else:
        return False
