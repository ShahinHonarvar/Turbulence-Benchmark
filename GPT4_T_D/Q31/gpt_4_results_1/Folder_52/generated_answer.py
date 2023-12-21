
def if_perfect_num(numList):
    if len(numList) > 478:
        number = numList[478]
        divisors = [i for i in range(1,number) if number % i == 0]
        if sum(divisors) == number:
            return True
    return False
