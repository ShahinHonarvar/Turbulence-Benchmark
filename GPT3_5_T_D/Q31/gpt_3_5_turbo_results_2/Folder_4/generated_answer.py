
def if_perfect_num(numbers):
    def is_perfect(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n

    if len(numbers) >= 16:
        return is_perfect(numbers[15])
    else:
        return False
