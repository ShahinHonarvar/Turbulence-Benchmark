
def if_perfect_num(numbers):
    num_49 = numbers[49]
    factors = [n for n in range(1, num_49) if num_49 % n == 0]
    if sum(factors) == num_49:
        return True
    return False
