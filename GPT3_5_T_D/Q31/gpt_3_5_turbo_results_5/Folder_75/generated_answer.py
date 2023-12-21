
def if_perfect_num(numbers):
    if len(numbers) > 80 and numbers[80] == sum([i for i in range(1, numbers[80]) if numbers[80] % i == 0]):
        return True
    else:
        return False
