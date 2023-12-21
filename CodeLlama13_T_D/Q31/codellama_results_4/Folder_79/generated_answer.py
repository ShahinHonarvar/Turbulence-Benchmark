
def if_perfect_num(numbers):
    if len(numbers) < 63:
        return False
    else:
        n = numbers[62]
        sum_of_divisors = 0
        for i in range(1, n):
            if n % i == 0:
                sum_of_divisors += i
        if sum_of_divisors == n:
            return True
        else:
            return False
