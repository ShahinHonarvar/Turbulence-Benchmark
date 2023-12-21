
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num

    if len(numbers) > 33:
        return is_perfect(numbers[33])
    else:
        return False
