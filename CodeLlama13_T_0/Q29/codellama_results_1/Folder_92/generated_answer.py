
def gcf_two_nums(numbers):
    return numbers[0] if numbers[1] % numbers[0] == 0 else gcf_two_nums([numbers[1], numbers[0]])
