
def if_perfect_num(numbers):
    if len(numbers) > 18:
        number = numbers[18]
        sum = 1
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                sum = sum + i + number/i
        return sum == number
    return False
