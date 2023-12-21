
def if_perfect_num(numbers):
    if len(numbers) > 63:
        num = numbers[63]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
