
def if_perfect_num(numbers):
    if numbers[27] == sum(filter(lambda x: x != 0 and numbers[27] % x == 0, range(1, int(numbers[27]) ** 0.5 + 1))):
        return True
    else:
        return False
