
def if_perfect_num(numbers):
    def is_perfect_num(num):
        divisors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                divisors.extend([i, num//i])
        return sum(divisors) == num

    if len(numbers) > 95:
        return is_perfect_num(numbers[95])
    else:
        return False
