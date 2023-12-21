
def if_perfect_num(numbers):
    if len(numbers) <= 99:
        return False
    num = numbers[99]
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    return sum_divisors == num
