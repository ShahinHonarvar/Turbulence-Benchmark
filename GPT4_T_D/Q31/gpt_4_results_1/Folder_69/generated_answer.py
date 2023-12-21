
def if_perfect_num(numbers):
    if len(numbers) <= 459:
        return False
    num = numbers[459]
    divisors = [i for i in range(1,num) if num % i == 0]
    return sum(divisors) == num
