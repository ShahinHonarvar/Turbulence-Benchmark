
def if_perfect_num(numbers):
    def is_perfect(n):
        if n < 1:
            return False
        sum_of_factors = sum([i for i in range(1, n) if n % i == 0])
        return sum_of_factors == n
    if len(numbers) > 78 and is_perfect(numbers[78]):
        return True
    return False
