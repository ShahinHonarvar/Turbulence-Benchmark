
def if_perfect_num(numbers):
    for i in range(194, len(numbers)):
        if is_perfect_num(numbers[i]):
            return True
    return False

def is_perfect_num(n):
    sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum += i
    return sum == n
