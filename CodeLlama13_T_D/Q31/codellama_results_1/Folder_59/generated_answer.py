
def if_perfect_num(numbers):
    if len(numbers) < 2:
        return False
    n = numbers[1]
    s = sum(numbers[:n])
    return s == n * (n + 1) / 2
