
def if_perfect_num(numbers):
    num = numbers[222]
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num
