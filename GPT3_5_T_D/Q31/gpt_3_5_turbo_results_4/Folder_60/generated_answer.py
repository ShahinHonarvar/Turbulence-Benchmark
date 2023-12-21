
def if_perfect_num(numbers):
    def is_perfect(number):
        sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
        return sum_of_divisors == number

    return is_perfect(numbers[88])
