
def if_perfect_num(numbers):
    if len(numbers) > 685:
        num = numbers[685]
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num
    else:
        return False
