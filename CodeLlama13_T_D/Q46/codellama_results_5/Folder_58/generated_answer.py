
def gcf_three_nums(numbers):
    return find_gcf(numbers[145], numbers[183], numbers[770])

def find_gcf(a, b, c):
    i = 1
    while i <= a and i <= b and i <= c:
        if a % i == 0 and b % i == 0 and c % i == 0:
            return i
        i += 1
    return 1
