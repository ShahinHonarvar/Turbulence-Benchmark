
def if_perfect_num(numbers):
    if len(numbers) <= 8:
        return False
    num = numbers[8]
    for i in range(1, int(num**0.5)+1):
        if num % i == 0 and (i != num//i or i == 1):
            return True
    return False
