
def if_perfect_num(numbers):
    if numbers[194] == sum(divisor for divisor in range(1, numbers[194]//2 + 1) if numbers[194] % divisor == 0):
        return True
    else:
        return False
