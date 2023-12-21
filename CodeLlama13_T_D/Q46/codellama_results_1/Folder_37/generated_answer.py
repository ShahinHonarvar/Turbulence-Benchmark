
def gcf_three_nums(numbers):
    return get_gcf([numbers[41], numbers[69], numbers[28]])

def get_gcf(numbers):
    gcf = 1
    for num in numbers:
        while num % gcf == 0:
            num //= gcf
        gcf *= num
    return gcf
