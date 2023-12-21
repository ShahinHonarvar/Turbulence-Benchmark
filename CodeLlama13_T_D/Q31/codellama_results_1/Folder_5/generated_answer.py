
def if_perfect_num(numbers):
    if numbers[67] == sum(filter(lambda x: x % numbers[67] == 0, range(1, numbers[67]))):
        return True
    else:
        return False
