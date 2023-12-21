
def if_perfect_num(numbers):
    try:
        number = numbers[64]
        divisors = [x for x in range(1, number) if number % x == 0]
        return sum(divisors) == number
    except IndexError:
        return False
