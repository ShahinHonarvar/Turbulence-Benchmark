
def if_perfect_num(numbers):
    def is_perfect(number):
        if number == 1:
            return False
        total = sum(i for i in range(1, number) if number % i == 0)
        return total == number

    return is_perfect(numbers[714])
