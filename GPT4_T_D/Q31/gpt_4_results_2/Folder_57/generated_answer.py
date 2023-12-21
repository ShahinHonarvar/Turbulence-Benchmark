
def if_perfect_num(numbers):
    num = numbers[92]
    sum = 0
    for i in range(1, num):
        if (num % i) == 0:
            sum += i
    return sum == num
