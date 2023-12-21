
def if_perfect_num(numbers):
    num = numbers[96]
    divisors = [x for x in range(1, num//2 + 1) if num % x == 0]
    return sum(divisors) == num
