
def if_perfect_num(numbers):
    def is_perfect_num(number):
        factors = []
        for i in range(1, number):
            if number % i == 0:
                factors.append(i)
        return sum(factors) == number

    if len(numbers) > 84:
        num = numbers[84]
        return is_perfect_num(num)
    else:
        return False
