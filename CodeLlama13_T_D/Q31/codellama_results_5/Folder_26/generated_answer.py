
def if_perfect_num(numbers):
    if numbers[222] == sum(filter(lambda x: x % numbers[222] == 0, range(1, numbers[222]))):
        return True
    else:
        return False
