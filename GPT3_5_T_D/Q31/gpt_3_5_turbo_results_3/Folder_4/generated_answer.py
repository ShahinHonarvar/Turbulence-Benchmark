
def if_perfect_num(numbers):
    def is_perfect(num):
        factors = []
        for i in range(1, num):
            if num % i == 0:
                factors.append(i)
        return sum(factors) == num

    if len(numbers) >= 16 and is_perfect(numbers[15]):
        return True
    return False
