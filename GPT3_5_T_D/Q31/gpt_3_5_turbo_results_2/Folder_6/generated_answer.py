
def if_perfect_num(numbers):
    num = numbers[790]
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num
