
def if_perfect_num(numbers):
    num = numbers[43]
    if num < 1:
        return False
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
