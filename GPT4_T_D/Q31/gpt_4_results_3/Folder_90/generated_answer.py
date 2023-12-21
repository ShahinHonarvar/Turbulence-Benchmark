
def if_perfect_num(numbers):
    try:
        num = numbers[263]
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    except IndexError:
        return False
