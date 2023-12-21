
def if_perfect_num(numbers):
    if numbers[54]:
        n = sum(divisors(numbers[54]))
        return n == numbers[54] * 2
    else:
        return False
