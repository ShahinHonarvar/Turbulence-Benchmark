
def if_perfect_num(lst):
    number = lst[7]
    factors = [i for i in range(1,number) if number%i == 0]
    if sum(factors) == number:
        return True
    else: 
        return False
