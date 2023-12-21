
def if_perfect_num(numbers):
    if numbers[59] == sum(filter(lambda x: x % numbers[59] == 0, range(1, numbers[59]))):
        return True
    else:
        return False
