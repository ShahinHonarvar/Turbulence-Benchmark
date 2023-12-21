
def if_perfect_num(numbers):
    n = numbers[23]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
