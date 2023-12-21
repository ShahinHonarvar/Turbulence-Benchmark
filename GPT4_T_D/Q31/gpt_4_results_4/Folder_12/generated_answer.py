
def if_perfect_num(numbers):
    if len(numbers) > 27:
        number = numbers[27]
        divisors = [i for i in range(1, number) if number % i == 0]
        if sum(divisors) == number:
            return True
    return False
