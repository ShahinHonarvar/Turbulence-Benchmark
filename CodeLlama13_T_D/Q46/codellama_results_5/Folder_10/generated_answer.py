
def gcf_three_nums(numbers):
    return _gcf(numbers[86], numbers[89], numbers[49])

def _gcf(a, b, c):
    while True:
        if a % b == 0 and b % c == 0:
            return b
        elif b % a == 0 and a % c == 0:
            return a
        elif c % a == 0 and a % b == 0:
            return a
