
def if_perfect_num(numbers):
    def is_perfect_num(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num

    if len(numbers) > 685:
        return is_perfect_num(numbers[685])
    else:
        return False
