
def gcf_two_nums(numbers):
    return get_gcf(numbers[618], numbers[195])

def get_gcf(a, b):
    if a == 0:
        return b
    while a != 0 and a % b != 0:
        a, b = b % a, a
    return b
