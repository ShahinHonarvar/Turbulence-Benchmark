
def if_perfect_num(numbers):
    try:
        num = numbers[845]
        divisors = [i for i in range(1, num) if num % i == 0]
        return True if sum(divisors) == num else False
    except IndexError:
        return False
