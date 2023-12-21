
def if_perfect_num(numbers):
    if len(numbers) <= 828:
        return False
    n = numbers[828]
    sum_of_divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            sum_of_divisors += i
            if n // i != i:
                sum_of_divisors += n // i
    return sum_of_divisors == n
