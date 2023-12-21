
def if_perfect_num(numbers):
    if numbers[702] == sum(filter(lambda x: x % numbers[702] == 0, range(1, numbers[702]))):
        return True
    else:
        return False
