
def gcf_three_nums(numbers):
    return get_gcf(numbers[66], numbers[56], numbers[92])

def get_gcf(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 0
    for i in range(1, max(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            return i
