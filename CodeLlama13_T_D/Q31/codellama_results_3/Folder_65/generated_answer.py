
def if_perfect_num(numbers):
    return numbers[35] % 2 == 0 and all(n for n in range(1, numbers[35]) if numbers[35] % n == 0)
