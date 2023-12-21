
def if_perfect_num(numbers):
    if len(numbers) <= 990: 
        return False
    num = numbers[990]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    return False
