
def if_perfect_num(numbers):
    if len(numbers) <= 849:
        return False
    number = numbers[849]
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return True
    else:
        return False
