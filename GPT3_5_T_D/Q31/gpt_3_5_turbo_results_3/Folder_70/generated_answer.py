
def if_perfect_num(numbers):
    num = numbers[845]
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False
