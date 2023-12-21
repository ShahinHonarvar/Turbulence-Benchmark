
def if_perfect_num(list_of_num):
    num = list_of_num[54]
    factors = [i for i in range(1, num) if num % i == 0]
    if sum(factors) == num:
        return True
    else:
        return False
