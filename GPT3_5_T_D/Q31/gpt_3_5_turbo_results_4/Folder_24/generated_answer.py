
def if_perfect_num(numbers):
    num = numbers[74]
    divisor_sum = sum([x for x in range(1, num) if num % x == 0])
    return divisor_sum == num
