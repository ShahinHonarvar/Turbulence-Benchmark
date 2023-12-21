
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num

    if len(numbers) >= 47:
        if numbers[46] > 0:
            return is_perfect(numbers[46])
    return False
