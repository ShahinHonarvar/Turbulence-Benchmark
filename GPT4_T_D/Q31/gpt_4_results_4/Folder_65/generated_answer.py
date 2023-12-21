
def if_perfect_num(numbers):
    try:
        num = numbers[35]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    except IndexError:
        return False
