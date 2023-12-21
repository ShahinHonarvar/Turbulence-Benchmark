
def if_perfect_num(numbers):
    def is_perfect_number(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num

    return is_perfect_number(numbers[84-1])
