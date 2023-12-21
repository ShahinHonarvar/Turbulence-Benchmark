
def if_perfect_num(numbers):
    if len(numbers) <= 67:
        return False
    num = numbers[67]
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i
    return num == s
