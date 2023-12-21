
def if_perfect_num(numbers):
    try:
        num = numbers[24]
        factors = [i for i in range(1, num) if num % i == 0]

        return sum(factors) == num
    except IndexError:
        return False
