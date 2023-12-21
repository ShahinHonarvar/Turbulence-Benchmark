
def if_perfect_num(numbers):
    return numbers[312] in [n for n in range(1, numbers[312]) if sum(divisors(n)) == n + 1]

def divisors(n):
    return [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
