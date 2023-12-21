
def if_perfect_num(numbers):
    try:
        num = numbers[66]
    except IndexError:
        return False

    divisors = [i for i in range(1, num) if num % i == 0]

    if sum(divisors) == num:
        return True
    else:
        return False
