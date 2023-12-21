
def if_perfect_num(numbers):
    if numbers[38] == sum(set(range(1, int(numbers[38]) ** 0.5 + 1))) and all([int(numbers[38]) % i == 0 for i in range(2, int(numbers[38]) // 2 + 1)]):
        return True
    else:
        return False
