
def if_perfect_num(numbers):
    if len(numbers) <= 100:
        return False
    else:
        num = numbers[100]
        sum_divisors = 0
        for i in range(1, num):
            if num % i == 0 and i != num:
                sum_divisors += i
        if sum_divisors == num:
            return True
        else:
            return False
