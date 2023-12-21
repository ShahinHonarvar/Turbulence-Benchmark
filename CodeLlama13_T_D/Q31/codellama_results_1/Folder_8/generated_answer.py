
def if_perfect_num(numbers):
    return (numbers[49] == sum(divisors(numbers[49])) - numbers[49])

def divisors(n):
    return [i for i in range(1, n+1) if n % i == 0]
