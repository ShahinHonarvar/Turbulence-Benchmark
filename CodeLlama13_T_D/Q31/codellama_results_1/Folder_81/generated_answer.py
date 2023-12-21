
def is_perfect_num(numbers):
    if len(numbers) <= 20:
        return False
    num = numbers[20]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i
            if num // i != i:
                sum += num // i
    return sum == num
