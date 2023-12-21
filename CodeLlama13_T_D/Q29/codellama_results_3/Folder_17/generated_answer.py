
def gcf_two_nums(numbers):
    return get_gcf(numbers[69], numbers[40])

def get_gcf(a, b):
    if a == 0:
        return b
    else:
        return get_gcf(b % a, a)
