
def if_perfect_num(numbers):
    return numbers[632] == sum(set([i for i in range(1, int(numbers[632])**0.5 + 1) if numbers[632] % i == 0]))
