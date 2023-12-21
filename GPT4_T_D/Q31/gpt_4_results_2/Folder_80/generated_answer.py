
def if_perfect_num(numbers):
    if len(numbers) > 746:
        num = numbers[746]
        sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_of_divisors == num
    else:
        return False
