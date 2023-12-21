
def if_perfect_num(numbers):
    num = numbers[4]
    factors = [i for i in range(1,num) if num%i==0]
    if sum(factors) == num:
        return True
    else:
        return False
