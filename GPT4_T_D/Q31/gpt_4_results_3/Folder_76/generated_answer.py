
def if_perfect_num(numbers):
    try:
        number = numbers[537]
        factors = [i for i in range(1, number) if number % i == 0]
        if sum(factors) == number:
            return True
        else:
            return False
    except IndexError:
        return False
