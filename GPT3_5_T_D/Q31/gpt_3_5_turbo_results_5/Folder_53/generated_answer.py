
def if_perfect_num(numbers):
    num = numbers[73]
    divisor_sum = sum([i for i in range(1, num) if num % i == 0])
    return num == divisor_sum
