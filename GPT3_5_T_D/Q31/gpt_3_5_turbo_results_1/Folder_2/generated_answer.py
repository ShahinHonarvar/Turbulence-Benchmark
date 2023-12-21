
def if_perfect_num(numbers):
    if numbers[702] == sum(divisor for divisor in range(1, numbers[702]) if numbers[702] % divisor == 0):
        return True
    else:
        return False
