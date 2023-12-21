
def if_perfect_num(numbers):
    num = numbers[87]
    if num <= 0:
        return False

    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i

    return divisor_sum == num
