
def if_perfect_num(numbers):
    try:
        num = numbers[53]
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    except IndexError:
        return False
