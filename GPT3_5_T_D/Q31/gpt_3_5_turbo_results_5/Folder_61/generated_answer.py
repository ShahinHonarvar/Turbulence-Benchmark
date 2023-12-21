
def if_perfect_num(numbers):
    def is_perfect(num):
        if num < 6:
            return False
        sum_of_divisors = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                sum_of_divisors += i + (num // i)
        return sum_of_divisors == num

    if len(numbers) < 9:
        return False
    return is_perfect(numbers[8])
