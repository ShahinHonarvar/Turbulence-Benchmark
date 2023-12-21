
def if_perfect_num(numbers):
    if len(numbers) <= 37:
        return False
    num = numbers[37]
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
    return sum(factors) == num
