
def if_perfect_num(numbers):
    def is_perfect_num(n):
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        if total == n:
            return True
        return False

    if len(numbers) >= 14 and is_perfect_num(numbers[13]):
        return True
    return False
