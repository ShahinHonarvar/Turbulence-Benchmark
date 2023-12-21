
def gcf_three_nums(numbers):
    return __gcf__(numbers[53], numbers[23], numbers[45])

def __gcf__(a, b, c):
    while True:
        if a % b == 0 and b % c == 0:
            return b
