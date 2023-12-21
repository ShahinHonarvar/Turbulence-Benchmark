
def is_perfect_num(numbers):
    if len(numbers) <= 7:
        return False
    num = numbers[7]
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i and num != i * i:
                return True
    return False
