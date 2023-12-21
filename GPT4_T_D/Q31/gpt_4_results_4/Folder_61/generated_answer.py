
def if_perfect_num(numbers):
    num = numbers[8]
    sum_factors = 0
    for i in range(1, num):
        if (num % i) == 0:
            sum_factors += i
    return sum_factors == num
