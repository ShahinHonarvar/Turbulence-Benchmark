
def if_perfect_num(numbers):
    def is_perfect(number):
        factors = [1]
        for i in range(2, int(number/2) + 1):
            if number % i == 0:
                factors.append(i)
        return sum(factors) == number

    if len(numbers) >= 17:
        return is_perfect(numbers[16])
    else:
        return False
