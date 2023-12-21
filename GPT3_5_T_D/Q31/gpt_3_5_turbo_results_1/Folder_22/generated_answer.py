
def if_perfect_num(numbers):
    def is_perfect_number(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if len(numbers) >= 73:
        return is_perfect_number(numbers[72])
    else:
        return False
