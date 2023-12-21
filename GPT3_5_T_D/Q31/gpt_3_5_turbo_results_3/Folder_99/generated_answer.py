
def if_perfect_num(numbers):
    num = numbers[732]
    divisors = [i for i in range(1, num // 2 + 1) if num % i == 0]
    if sum(divisors) == num:
        return True
    return False
