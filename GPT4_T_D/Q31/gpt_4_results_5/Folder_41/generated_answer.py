
def if_perfect_num(numbers):
    if len(numbers) > 84:
        num = numbers[84]
        factor_sum = sum([i for i in range(1, num) if num % i == 0])
        return factor_sum == num
    return False
