
def if_perfect_num(numbers):
    return numbers[15] in [i for i in range(2, int(numbers[15]**0.5)+1) if numbers[15] % i == 0]
