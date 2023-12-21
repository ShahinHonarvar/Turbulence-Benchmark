
def if_perfect_num(numbers):
    num = numbers[24]
    sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])
    if sum_of_divisors == num:
        return True
    else:
        return False
