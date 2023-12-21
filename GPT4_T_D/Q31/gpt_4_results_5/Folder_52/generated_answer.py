
def if_perfect_num(lst):
    try:
        num = lst[478]
        divisors = [i for i in range(1,num) if num % i == 0]
        if num == sum(divisors):
            return True
        else:
            return False
    except IndexError:
        return False
