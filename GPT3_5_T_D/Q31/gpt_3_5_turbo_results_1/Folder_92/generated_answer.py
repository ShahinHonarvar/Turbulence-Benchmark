
def if_perfect_num(numbers):
    def is_perfect_num(number):
        divisors = []
        for i in range(1, number):
            if number % i == 0:
                divisors.append(i)
        return sum(divisors) == number

    return is_perfect_num(numbers[0])
