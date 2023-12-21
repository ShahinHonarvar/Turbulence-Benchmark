
def if_perfect_num(numbers):
    num = numbers[74]
    factors_sum = sum([i for i in range(1, num) if num % i == 0])
    return factors_sum == num
