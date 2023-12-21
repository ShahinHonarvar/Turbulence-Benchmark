
def if_perfect_num(numbers):
    if len(numbers) > 63:
        num = numbers[63]
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    else:
        return False
