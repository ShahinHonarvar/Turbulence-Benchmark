
def if_perfect_num(numbers):
    if len(numbers) > 96:
        value = numbers[96]
        factor_sum = sum(i for i in range(1, value) if value % i == 0)
        if factor_sum == value:
            return True
    return False
