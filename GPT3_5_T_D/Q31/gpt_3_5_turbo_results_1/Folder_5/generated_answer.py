
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors_sum = 0
        for i in range(1, num):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum == num

    return is_perfect(numbers[67])
