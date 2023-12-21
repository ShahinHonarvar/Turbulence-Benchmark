
def if_perfect_num(list_of_num):
    try:
        num = list_of_num[276]
        divisors = [i for i in range(1,num) if num%i==0]
        if sum(divisors) == num:
            return True
        else:
            return False
    except:
        return False
