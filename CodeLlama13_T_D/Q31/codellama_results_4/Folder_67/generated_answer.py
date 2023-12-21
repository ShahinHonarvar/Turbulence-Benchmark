
def if_perfect_num(numbers):
    if len(numbers) <= 43:
        return False
    num = numbers[43]
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0 and (i ** 2 != num or i != sqrt(num)):
            return False
    return True
