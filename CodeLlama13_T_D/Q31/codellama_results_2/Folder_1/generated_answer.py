
def if_perfect_num(numbers):
    n = numbers[85]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and i * (n // i) == n:
            return True
    return False
