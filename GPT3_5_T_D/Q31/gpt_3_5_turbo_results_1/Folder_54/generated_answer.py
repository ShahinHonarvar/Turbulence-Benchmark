
def if_perfect_num(numbers):
    def is_perfect_number(num):
        if num <= 0:
            return False
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        return divisors_sum == num

    return is_perfect_number(numbers[51])
