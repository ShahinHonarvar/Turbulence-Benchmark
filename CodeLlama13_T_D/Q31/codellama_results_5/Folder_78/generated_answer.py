
def if_perfect_num(numbers):
    for i in range(100, 100 + len(numbers)):
        n = numbers[i - 100]
        if n == sum(range(1, int(n ** 0.5) + 1)):
            return True
    return False
