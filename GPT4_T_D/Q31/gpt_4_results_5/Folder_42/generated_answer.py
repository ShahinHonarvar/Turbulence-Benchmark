
def if_perfect_num(numbers):
    if len(numbers) <= 276:
        return False

    num = numbers[276]
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        return True

    return False
