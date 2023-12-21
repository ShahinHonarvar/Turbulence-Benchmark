
def if_perfect_num(numbers):
    return (453 < len(numbers) and numbers[453] == sum(divisors(numbers[453])))

def divisors(n):
    return [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
