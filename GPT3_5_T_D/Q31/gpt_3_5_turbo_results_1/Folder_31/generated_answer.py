
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if numbers[66]:
        return is_perfect(numbers[66])
    else:
        return False
