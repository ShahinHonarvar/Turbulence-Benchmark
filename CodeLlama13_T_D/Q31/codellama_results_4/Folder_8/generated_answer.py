
def if_perfect_num(lst):
    if len(lst) <= 49:
        return False
    num = lst[49]
    for i in range(2, num):
        if num % i == 0 and sum(divisors(num)) == num + 1:
            return True
    return False
