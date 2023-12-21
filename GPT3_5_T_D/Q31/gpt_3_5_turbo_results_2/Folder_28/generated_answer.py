
def if_perfect_num(numbers):
    def is_perfect(number):
        divisors_sum = 1
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                divisors_sum += i + (number//i)

        if number != 1 and divisors_sum == number:
            return True
        else:
            return False

    try:
        if is_perfect(numbers[37]):
            return True
        else:
            return False
    except IndexError:
        return False
